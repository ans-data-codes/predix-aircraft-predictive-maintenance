"""Data loading interfaces for PREDIX."""

from pathlib import Path

import pandas as pd


def load_data(source: str | Path) -> pd.DataFrame:
    """Load raw data from a CSV/parquet source into a DataFrame.

    Args:
        source: File path or URI to the raw data source.

    Returns:
        Raw dataset as a pandas DataFrame.

    Raises:
        NotImplementedError: Placeholder until data connectors are implemented.
    """
    raise NotImplementedError("Data loading connector is not implemented yet.")


def validate_data(data: pd.DataFrame) -> tuple[bool, list[str]]:
    """Validate expected schema and quality checks on raw data.

    Args:
        data: Raw input dataset.

    Returns:
        Tuple with validation pass/fail and list of validation issues.

    Raises:
        NotImplementedError: Placeholder until validation rules are implemented.
    """
    raise NotImplementedError("Data validation rules are not implemented yet.")
