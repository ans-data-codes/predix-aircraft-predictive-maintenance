"""Data cleaning and preprocessing interfaces for PREDIX."""

import pandas as pd


def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    """Clean and preprocess validated raw data for downstream use.

    Args:
        data: Validated raw data.

    Returns:
        Cleaned and standardized data.

    Raises:
        NotImplementedError: Placeholder until preprocessing logic is implemented.
    """
    raise NotImplementedError("Preprocessing pipeline is not implemented yet.")
