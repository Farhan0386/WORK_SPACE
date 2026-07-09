import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "dataset.csv")
LINE_PLOT_PATH = os.path.join(BASE_DIR, "yearly_average_temperature.png")
HEATMAP_PATH = os.path.join(BASE_DIR, "temperature_heatmap.png")


def build_sample_dataset() -> pd.DataFrame:
    """Create a small climate dataset with 80 rows."""

    rng = np.random.default_rng(42)

    locations = {
        "India": {
            "Maharashtra": (19.1, 72.9, 28.0),
            "Tamil Nadu": (13.1, 80.3, 30.0),
        },
        "USA": {
            "California": (36.8, -119.4, 18.0),
            "Texas": (31.0, -99.9, 24.0),
        },
        "Brazil": {
            "Sao Paulo": (-23.5, -46.6, 22.0),
            "Bahia": (-12.9, -38.5, 27.0),
        },
        "Australia": {
            "New South Wales": (-33.9, 151.2, 16.0),
            "Queensland": (-20.9, 144.0, 25.0),
        },
    }

    timestamps = pd.date_range("2018-01-01", periods=10, freq="YS")
    rows = []

    for timestamp in timestamps:
        month_angle = 2 * np.pi * (timestamp.month - 1) / 12
        seasonal_effect = 4 * np.sin(month_angle)

        for country, states in locations.items():
            for state, (latitude, longitude, base_temp) in states.items():
                temperature = base_temp + seasonal_effect + rng.normal(0, 1.2)
                quality_flag = 0

                if rng.random() < 0.12:
                    temperature += rng.normal(7, 1)
                    quality_flag = 1

                rows.append(
                    {
                        "Timestamp": timestamp,
                        "Country": country,
                        "State": state,
                        "Latitude": latitude,
                        "Longitude": longitude,
                        "Temperature": round(float(temperature), 2),
                        "QualityFlag": quality_flag,
                    }
                )

    dataset = pd.DataFrame(rows)

    missing_indices = rng.choice(dataset.index, size=5, replace=False)
    dataset.loc[missing_indices, "Temperature"] = np.nan

    return dataset


def load_and_clean_dataset(file_path: str) -> pd.DataFrame:
    """Load the CSV, fill missing values, and clean flagged temperatures."""

    df = pd.read_csv(file_path)
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")

    df["Temperature"] = df["Temperature"].fillna(df["Temperature"].median())
    df["Latitude"] = df["Latitude"].fillna(df["Latitude"].median())
    df["Longitude"] = df["Longitude"].fillna(df["Longitude"].median())
    df["QualityFlag"] = df["QualityFlag"].fillna(0).astype(int)
    df = df.dropna(subset=["Timestamp", "Country", "State"])

    df = df.set_index(["Country", "State", "Timestamp"]).sort_index()

    working = df.reset_index().sort_values(["Country", "State", "Timestamp"])
    working["RollingMedian"] = working.groupby(["Country", "State"])[
        "Temperature"
    ].transform(lambda series: series.rolling(window=3, center=True, min_periods=1).median())

    working["Temperature"] = np.where(
        working["QualityFlag"] == 1, working["RollingMedian"], working["Temperature"]
    )
    working = working.drop(columns=["RollingMedian"])

    return working.set_index(["Country", "State", "Timestamp"]).sort_index()


def create_yearly_average_plot(df: pd.DataFrame) -> None:
    yearly_average = df["Temperature"].groupby(pd.Grouper(level="Timestamp", freq="YE")).mean()

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(yearly_average.index.year, yearly_average.values, marker="o", color="tomato")
    ax.set_title("Yearly Average Temperature")
    ax.set_xlabel("Year")
    ax.set_ylabel("Temperature (C)")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(LINE_PLOT_PATH, dpi=150)
    plt.close(fig)


def create_heatmap(df: pd.DataFrame) -> None:
    summary = (
        df.reset_index()
        .assign(Year=lambda frame: frame["Timestamp"].dt.year)
        .groupby(["Country", "State", "Year"])["Temperature"]
        .mean()
        .unstack("Year")
        .sort_index()
    )

    fig, ax = plt.subplots(figsize=(10, 6))
    image = ax.imshow(summary.values, aspect="auto", cmap="coolwarm")
    ax.set_title("Temperature Heatmap")
    ax.set_xlabel("Year")
    ax.set_ylabel("Country / State")
    ax.set_xticks(range(len(summary.columns)))
    ax.set_xticklabels(summary.columns.astype(str), rotation=45, ha="right")
    ax.set_yticks(range(len(summary.index)))
    ax.set_yticklabels([f"{country} - {state}" for country, state in summary.index])
    fig.colorbar(image, ax=ax, label="Temperature (C)")
    fig.tight_layout()
    fig.savefig(HEATMAP_PATH, dpi=150)
    plt.close(fig)


def main() -> None:
    dataset = build_sample_dataset()
    dataset.to_csv(DATASET_PATH, index=False)

    cleaned_data = load_and_clean_dataset(DATASET_PATH)
    create_yearly_average_plot(cleaned_data)
    create_heatmap(cleaned_data)

    print(f"Created dataset: {DATASET_PATH}")
    print(f"Saved plot: {LINE_PLOT_PATH}")
    print(f"Saved plot: {HEATMAP_PATH}")
    print("Cleaned data preview:")
    print(cleaned_data.head())


if __name__ == "__main__":
    main()