from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any, Optional, Union

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt


TARGET_NAMES = ("churn", "exited", "attrition", "is_churn")


def create_demo_data() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "customer_id": ["C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008"],
            "gender": ["Female", "Male", "Female", "Male", np.nan, "Female", "Male", "Female"],
            "contract": ["Month-to-month", "One year", "Month-to-month", "Two year", "Month-to-month", "One year", "Month-to-month", "Two year"],
            "tenure": [2, 24, 5, 48, 1, 18, 3, 36],
            "monthly_charges": [70.5, 55.2, 92.1, 45.0, 88.4, 64.8, 105.0, 52.7],
            "total_charges": [141.0, 1324.8, np.nan, 2160.0, 88.4, 1166.4, 315.0, 1897.2],
            "churn": ["Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No"],
        }
    )


def load_customer_data(file_path: Optional[Union[str, Path]] = None) -> pd.DataFrame:
    if file_path is None:
        return create_demo_data()

    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"Customer churn file was not found: {path}")
    return pd.read_csv(path)


def find_churn_column(data: pd.DataFrame) -> str:
    normalized_names = {column.strip().lower(): column for column in data.columns}
    for target_name in TARGET_NAMES:
        if target_name in normalized_names:
            return normalized_names[target_name]
    raise ValueError("The dataset must contain a churn target column such as 'Churn' or 'Exited'.")


def clean_customer_data(data: pd.DataFrame, churn_column: str) -> pd.DataFrame:
    cleaned_data = data.copy()
    cleaned_data.columns = [column.strip().lower().replace(" ", "_") for column in cleaned_data.columns]
    churn_column = churn_column.strip().lower().replace(" ", "_")

    for column in cleaned_data.select_dtypes(include="object").columns:
        cleaned_data[column] = cleaned_data[column].astype("string").str.strip()
        cleaned_data[column] = cleaned_data[column].replace({"": pd.NA, "nan": pd.NA, "none": pd.NA})

    for column in cleaned_data.columns:
        if column == churn_column:
            continue
        numeric_values = pd.to_numeric(cleaned_data[column], errors="coerce")
        if numeric_values.notna().mean() >= 0.8:
            cleaned_data[column] = numeric_values

    for column in cleaned_data.select_dtypes(include=np.number).columns:
        cleaned_data[column] = cleaned_data[column].fillna(cleaned_data[column].median())

    for column in cleaned_data.select_dtypes(include=["object", "string", "category"]).columns:
        most_common = cleaned_data[column].mode(dropna=True)
        replacement = most_common.iloc[0] if not most_common.empty else "Unknown"
        cleaned_data[column] = cleaned_data[column].fillna(replacement)

    cleaned_data[churn_column] = cleaned_data[churn_column].astype("string").str.strip().str.lower()
    cleaned_data["churn_flag"] = cleaned_data[churn_column].map(
        {"yes": 1, "true": 1, "1": 1, "y": 1, "no": 0, "false": 0, "0": 0, "n": 0}
    )
    if cleaned_data["churn_flag"].isna().any():
        raise ValueError("The churn target must contain recognizable Yes/No or True/False values.")

    return cleaned_data


def create_summary_statistics(data: pd.DataFrame, churn_column: str) -> dict[str, Any]:
    numeric_columns = data.select_dtypes(include=np.number).columns.tolist()
    numeric_columns = [column for column in numeric_columns if column != "churn_flag"]
    numeric_summary = data[numeric_columns].describe().T if numeric_columns else pd.DataFrame()
    churn_rate = float(data["churn_flag"].mean() * 100)
    missing_values = data.isna().sum().sort_values(ascending=False)
    churn_counts = data[churn_column].value_counts(dropna=False)

    return {
        "row_count": len(data),
        "column_count": len(data.columns),
        "churn_rate_percent": churn_rate,
        "churn_counts": churn_counts,
        "missing_values": missing_values[missing_values > 0],
        "numeric_summary": numeric_summary,
    }


def find_significant_patterns(data: pd.DataFrame, churn_column: str) -> pd.DataFrame:
    patterns: list[dict[str, Any]] = []
    for column in data.select_dtypes(include=["object", "string", "category"]).columns:
        if column in {churn_column, "customer_id"}:
            continue
        grouped = data.groupby(column, dropna=False)["churn_flag"].agg(["mean", "count"])
        if len(grouped) > 1:
            difference = float((grouped["mean"].max() - grouped["mean"].min()) * 100)
            highest_group = str(grouped["mean"].idxmax())
            patterns.append(
                {
                    "feature": column,
                    "pattern": f"{highest_group} has the highest churn rate",
                    "highest_churn_rate_percent": float(grouped["mean"].max() * 100),
                    "rate_difference_percent": difference,
                }
            )

    for column in data.select_dtypes(include=np.number).columns:
        if column == "churn_flag":
            continue
        correlation = data[[column, "churn_flag"]].corr().iloc[0, 1]
        if pd.notna(correlation):
            patterns.append(
                {
                    "feature": column,
                    "pattern": "Positive relationship with churn" if correlation > 0 else "Negative relationship with churn",
                    "highest_churn_rate_percent": np.nan,
                    "rate_difference_percent": abs(float(correlation)) * 100,
                }
            )

    return pd.DataFrame(patterns).sort_values("rate_difference_percent", ascending=False) if patterns else pd.DataFrame()


def create_churn_visualizations(data: pd.DataFrame, churn_column: str, output_folder: Union[str, Path]) -> list[Path]:
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)
    chart_paths: list[Path] = []

    churn_labels = data[churn_column].value_counts()
    figure, axis = plt.subplots(figsize=(7, 5))
    axis.bar(
        churn_labels.index.astype(str),
        churn_labels.to_numpy(dtype=float),
        color=["#4c78a8", "#e45756"][: len(churn_labels)],
    )
    axis.set_title("Customer churn distribution")
    axis.set_xlabel("Churn")
    axis.set_ylabel("Customers")
    figure.tight_layout()
    chart_path = output_path / "churn_distribution.png"
    figure.savefig(str(chart_path), dpi=150)
    plt.close(figure)
    chart_paths.append(chart_path)

    numeric_columns = [column for column in data.select_dtypes(include=np.number).columns if column != "churn_flag"]
    if numeric_columns:
        selected_columns = numeric_columns[: min(4, len(numeric_columns))]
        figure, axes = plt.subplots(1, len(selected_columns), figsize=(5 * len(selected_columns), 4))
        axes = np.atleast_1d(axes)
        for axis, column in zip(axes, selected_columns):
            data.boxplot(column=column, by=churn_column, ax=axis, grid=False)
            axis.set_title(f"{column} by churn")
            axis.set_xlabel("Churn")
            axis.set_ylabel(column)
        figure.suptitle("")
        figure.tight_layout()
        chart_path = output_path / "numeric_features_by_churn.png"
        figure.savefig(str(chart_path), dpi=150)
        plt.close(figure)
        chart_paths.append(chart_path)

    categorical_columns = [
        column
        for column in data.select_dtypes(include=["object", "string", "category"]).columns
        if column not in {churn_column, "customer_id"}
    ]
    if categorical_columns:
        selected_columns = categorical_columns[: min(3, len(categorical_columns))]
        figure, axes = plt.subplots(1, len(selected_columns), figsize=(6 * len(selected_columns), 4))
        axes = np.atleast_1d(axes)
        for axis, column in zip(axes, selected_columns):
            churn_rates = data.groupby(column, dropna=False)["churn_flag"].mean().mul(100).sort_values(ascending=False)
            axis.bar(churn_rates.index.astype(str), churn_rates.to_numpy(dtype=float), color="#f58518")
            axis.set_title(f"Churn rate by {column}")
            axis.set_xlabel(column)
            axis.set_ylabel("Churn rate (%)")
            axis.tick_params(axis="x", rotation=35)
        figure.tight_layout()
        chart_path = output_path / "categorical_churn_patterns.png"
        figure.savefig(str(chart_path), dpi=150)
        plt.close(figure)
        chart_paths.append(chart_path)

    return chart_paths


def run_churn_eda(
    file_path: Optional[Union[str, Path]] = None,
    output_folder: Union[str, Path] = "eda_output",
) -> dict[str, Any]:
    raw_data = load_customer_data(file_path)
    original_churn_column = find_churn_column(raw_data)
    cleaned_data = clean_customer_data(raw_data, original_churn_column)
    churn_column = original_churn_column.strip().lower().replace(" ", "_")
    summary = create_summary_statistics(cleaned_data, churn_column)
    patterns = find_significant_patterns(cleaned_data, churn_column)
    chart_paths = create_churn_visualizations(cleaned_data, churn_column, output_folder)

    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)
    cleaned_data.to_csv(output_path / "cleaned_customer_churn.csv", index=False)
    patterns.to_csv(output_path / "significant_churn_patterns.csv", index=False)

    print(f"Rows analyzed: {summary['row_count']}")
    print(f"Columns analyzed: {summary['column_count']}")
    print(f"Churn rate: {summary['churn_rate_percent']:.2f}%")
    print("\nNumeric summary:")
    print(summary["numeric_summary"].round(2).to_string())
    print("\nSignificant patterns:")
    print(patterns.head(10).round(2).to_string(index=False) if not patterns.empty else "No patterns were identified.")
    print(f"\nSaved {len(chart_paths)} visualizations to {output_path}")

    return {"cleaned_data": cleaned_data, "summary": summary, "patterns": patterns, "chart_paths": chart_paths}


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Explore and visualize a customer churn dataset.")
    parser.add_argument("--file", type=Path, help="Path to a customer churn CSV file.")
    parser.add_argument("--output", type=Path, default=Path("eda_output"), help="Folder for cleaned data and charts.")
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_arguments()
    run_churn_eda(arguments.file, arguments.output)
