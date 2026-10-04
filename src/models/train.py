"""Training interfaces for Remaining Useful Life (RUL) models."""

from typing import Any

import pandas as pd


def train_rul_model(features: pd.DataFrame, targets: pd.Series) -> Any:
    """Train an RUL prediction model.

    Args:
        features: Engineered feature matrix.
        targets: Ground truth RUL labels.

    Returns:
        Trained model object.

    Raises:
        NotImplementedError: Placeholder until training workflow is implemented.
    """
    raise NotImplementedError("RUL model training is not implemented yet.")
