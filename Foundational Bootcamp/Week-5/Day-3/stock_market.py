import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "stock_dataset.csv")
OHLC_PATH = os.path.join(BASE_DIR, "ohlc_chart.png")
VOLUME_PATH = os.path.join(BASE_DIR, "volume_chart.png")


def build_stock_dataset() -> pd.DataFrame:
    """Create a simple stock dataset with 60 rows."""

    rng = np.random.default_rng(7)

    tickers = ["ALFA", "BETA", "CORA"]
    actions = ["BUY", "SELL", "HOLD"]
    timestamps = pd.date_range("2025-01-01 09:30", periods=20, freq="D")

    rows = []
    for ticker_index, ticker in enumerate(tickers):
        base_price = 100 + ticker_index * 25
        for time_index, timestamp in enumerate(timestamps):
            trend = time_index * 0.6
            noise = rng.normal(0, 1.5)
            price = round(base_price + trend + noise, 2)
            volume = int(rng.integers(800, 4000))
            action = actions[(time_index + ticker_index) % len(actions)]

            rows.append(
                {
                    "Timestamp": timestamp,
                    "Ticker": ticker,
                    "Action": action,
                    "Price": price,
                    "Volume": volume,
                }
            )

    return pd.DataFrame(rows)


def load_and_prepare_data(file_path: str) -> pd.DataFrame:
    """Load the CSV and prepare it for analysis."""

    df = pd.read_csv(file_path)
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
    df["Price"] = df["Price"].fillna(df["Price"].median())
    df["Volume"] = df["Volume"].fillna(df["Volume"].median())
    df["Action"] = df["Action"].fillna("HOLD")
    df = df.dropna(subset=["Timestamp", "Ticker"])
    return df.sort_values(["Ticker", "Timestamp"]).reset_index(drop=True)


def calculate_vwap(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate VWAP for each ticker."""

    summary = (
        df.assign(TradeValue=df["Price"] * df["Volume"])
        .groupby("Ticker")
        .agg(TotalTradeValue=("TradeValue", "sum"), TotalVolume=("Volume", "sum"))
    )
    summary["VWAP"] = summary["TotalTradeValue"] / summary["TotalVolume"]
    return summary.reset_index()


def show_market_depth(df: pd.DataFrame) -> pd.DataFrame:
    """Use np.searchsorted() to bucket trades into simple price levels."""

    price_levels = np.arange(90, 181, 10)
    depth_rows = []

    for ticker, group in df.groupby("Ticker"):
        bucket_positions = np.searchsorted(price_levels, group["Price"].to_numpy(), side="right") - 1
        bucket_positions = np.clip(bucket_positions, 0, len(price_levels) - 1)
        grouped_depth = np.bincount(
            bucket_positions,
            weights=group["Volume"].to_numpy(),
            minlength=len(price_levels),
        )

        for level, volume in zip(price_levels, grouped_depth):
            depth_rows.append({"Ticker": ticker, "PriceLevel": level, "DepthVolume": int(volume)})

    return pd.DataFrame(depth_rows)


def create_ohlc_chart(df: pd.DataFrame) -> None:
    """Draw a simple OHLC-style chart without external finance libraries."""

    sample = df[df["Ticker"] == "ALFA"].copy()
    sample["Date"] = sample["Timestamp"].dt.date

    ohlc = sample.groupby("Date").agg(
        Open=("Price", "first"),
        High=("Price", "max"),
        Low=("Price", "min"),
        Close=("Price", "last"),
    )

    fig, ax = plt.subplots(figsize=(11, 5))
    x_values = np.arange(len(ohlc))

    for x_value, (_, row) in zip(x_values, ohlc.iterrows()):
        color = "green" if row["Close"] >= row["Open"] else "red"
        ax.vlines(x_value, row["Low"], row["High"], color=color, linewidth=1.5)
        ax.hlines(row["Open"], x_value - 0.2, x_value, color=color, linewidth=3)
        ax.hlines(row["Close"], x_value, x_value + 0.2, color=color, linewidth=3)

    ax.set_title("ALFA Simple OHLC Chart")
    ax.set_xlabel("Day")
    ax.set_ylabel("Price")
    ax.set_xticks(x_values)
    ax.set_xticklabels([str(date) for date in ohlc.index], rotation=45, ha="right")
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(OHLC_PATH, dpi=150)
    plt.close(fig)


def create_volume_chart(df: pd.DataFrame) -> None:
    """Draw a simple volume bar chart."""

    volume_by_ticker = df.groupby("Ticker")["Volume"].sum()

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(volume_by_ticker.index, volume_by_ticker.values, color=["steelblue", "orange", "seagreen"])
    ax.set_title("Total Volume by Ticker")
    ax.set_xlabel("Ticker")
    ax.set_ylabel("Volume")
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(VOLUME_PATH, dpi=150)
    plt.close(fig)


def main() -> None:
    dataset = build_stock_dataset()
    dataset.to_csv(DATASET_PATH, index=False)

    cleaned_data = load_and_prepare_data(DATASET_PATH)
    vwap_summary = calculate_vwap(cleaned_data)
    market_depth = show_market_depth(cleaned_data)

    create_ohlc_chart(cleaned_data)
    create_volume_chart(cleaned_data)

    print(f"Created dataset: {DATASET_PATH}")
    print(f"Rows in dataset: {len(dataset)}")
    print("VWAP by ticker:")
    print(vwap_summary)
    print("Simple market depth sample:")
    print(market_depth.head(9))
    print(f"Saved plot: {OHLC_PATH}")
    print(f"Saved plot: {VOLUME_PATH}")


if __name__ == "__main__":
    main()