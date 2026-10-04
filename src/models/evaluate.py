"""Evaluation interfaces for model quality tracking."""

from collections.abc import Mapping
from typing import Any

import pandas as pd


def evaluate_model(model: Any, features: pd.DataFrame, targets: pd.Series) -> Mapping[str, float]:
    """Evaluate an RUL model on validation/test data.

    Args:
        model: Trained model instance.
        features: Evaluation feature matrix.
        targets: Evaluation ground-truth labels.

    Returns:
        Dictionary of evaluation metrics.

    Raises:
        NotImplementedError: Placeholder until evaluation logic is implemented.
    """
    raise NotImplementedError("Model evaluation is not implemented yet.")
