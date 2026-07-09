import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "ecommerce_dataset.csv")
HEATMAP_PATH = os.path.join(BASE_DIR, "retention_heatmap.png")


def build_ecommerce_dataset() -> pd.DataFrame:
    """Create a small ecommerce dataset with 80 rows."""

    rng = np.random.default_rng(21)

    customers = ["C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008", "C009", "C010"]
    stock_codes = ["A100", "B200", "C300", "D400", "E500"]

    rows = []
    invoice_number = 50000

    for customer_index, customer_id in enumerate(customers):
        start_month = 1 + (customer_index % 4)

        monthly_rows = []
        for order_index in range(10):
            month = start_month + order_index
            if month > 12:
                month -= 12

            invoice_date = pd.Timestamp(year=2025, month=month, day=1) + pd.Timedelta(days=customer_index + order_index)
            quantity = int(rng.integers(1, 6))
            unit_price = round(float(rng.uniform(8, 60)), 2)

            monthly_rows.append(
                {
                    "InvoiceNo": f"INV{invoice_number}",
                    "CustomerID": customer_id,
                    "StockCode": stock_codes[(customer_index + order_index) % len(stock_codes)],
                    "Quantity": quantity,
                    "UnitPrice": unit_price,
                    "InvoiceDate": invoice_date,
                }
            )
            invoice_number += 1

        kept_rows = [monthly_rows[0]]
        remaining_rows = monthly_rows[1:]
        kept_indices = rng.choice(len(remaining_rows), size=7, replace=False)
        kept_rows.extend(remaining_rows[index] for index in sorted(kept_indices))
        rows.extend(kept_rows)

    return pd.DataFrame(rows)


def load_and_prepare_data(file_path: str) -> pd.DataFrame:
    """Load the CSV and prepare the date fields."""

    df = pd.read_csv(file_path)
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
    df = df.dropna(subset=["InvoiceDate", "CustomerID"])
    df["InvoiceMonth"] = df["InvoiceDate"].dt.to_period("M")
    return df.sort_values(["CustomerID", "InvoiceDate"]).reset_index(drop=True)


def add_cohort_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Create first purchase month and cohort month."""

    df = df.copy()
    df["FirstPurchaseMonth"] = df.groupby("CustomerID")["InvoiceDate"].transform("min").dt.to_period("M")
    df["CohortMonth"] = df["FirstPurchaseMonth"]
    df["CohortIndex"] = (df["InvoiceMonth"].dt.year - df["CohortMonth"].dt.year) * 12 + (
        df["InvoiceMonth"].dt.month - df["CohortMonth"].dt.month
    )
    return df


def create_retention_table(df: pd.DataFrame) -> pd.DataFrame:
    """Create a simple retention table using pivot_table()."""

    cohort_counts = df.pivot_table(
        index="CohortMonth",
        columns="CohortIndex",
        values="CustomerID",
        aggfunc="nunique",
    )

    cohort_sizes = cohort_counts.iloc[:, 0]
    retention = cohort_counts.divide(cohort_sizes, axis=0) * 100
    return retention


def calculate_cumulative_spending(df: pd.DataFrame) -> pd.DataFrame:
    """Use np.cumsum() to calculate cumulative customer spending."""

    spending = df.copy()
    spending["LineTotal"] = spending["Quantity"] * spending["UnitPrice"]
    spending = spending.sort_values(["CustomerID", "InvoiceDate"])
    spending["CumulativeSpending"] = spending.groupby("CustomerID")["LineTotal"].transform(np.cumsum)
    return spending


def create_retention_heatmap(retention: pd.DataFrame) -> None:
    """Draw a simple retention heatmap with matplotlib.imshow()."""

    fig, ax = plt.subplots(figsize=(10, 5))
    image = ax.imshow(retention.fillna(0).values, cmap="Blues", aspect="auto")
    ax.set_title("Customer Retention Heatmap")
    ax.set_xlabel("Months Since First Purchase")
    ax.set_ylabel("Cohort Month")
    ax.set_xticks(range(len(retention.columns)))
    ax.set_xticklabels([str(int(month)) for month in retention.columns])
    ax.set_yticks(range(len(retention.index)))
    ax.set_yticklabels([str(month) for month in retention.index])
    fig.colorbar(image, ax=ax, label="Retention %")

    for row_index in range(retention.shape[0]):
        for col_index in range(retention.shape[1]):
            value = retention.fillna(0).iloc[row_index, col_index]
            ax.text(col_index, row_index, f"{value:.0f}%", ha="center", va="center", color="black", fontsize=8)

    fig.tight_layout()
    fig.savefig(HEATMAP_PATH, dpi=150)
    plt.close(fig)


def main() -> None:
    dataset = build_ecommerce_dataset()
    dataset.to_csv(DATASET_PATH, index=False)

    prepared = load_and_prepare_data(DATASET_PATH)
    prepared = add_cohort_columns(prepared)
    retention = create_retention_table(prepared)
    spending = calculate_cumulative_spending(prepared)

    create_retention_heatmap(retention)

    print(f"Created dataset: {DATASET_PATH}")
    print(f"Rows in dataset: {len(dataset)}")
    print("Retention table:")
    print(retention.round(1))
    print("Cumulative spending sample:")
    print(spending[["CustomerID", "InvoiceDate", "LineTotal", "CumulativeSpending"]].head(10))
    print(f"Saved plot: {HEATMAP_PATH}")


if __name__ == "__main__":
    main()