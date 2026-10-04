"""Prediction and health scoring interfaces for PREDIX."""

from dataclasses import dataclass
from typing import Any

import pandas as pd


@dataclass(frozen=True)
class RULPredictionResult:
    """Container for RUL and aircraft/component health output."""

    predicted_rul: float
    health_score: float
    anomaly_flag: bool


def predict_rul(model: Any, features: pd.DataFrame) -> pd.Series:
    """Predict Remaining Useful Life from model-ready features.

    Args:
        model: Trained RUL model.
        features: Feature matrix for inference.

    Returns:
        Predicted RUL values.

    Raises:
        NotImplementedError: Placeholder until inference logic is implemented.
    """
    raise NotImplementedError("RUL prediction is not implemented yet.")


def calculate_health_score(predicted_rul: pd.Series) -> pd.Series:
    """Convert predicted RUL into a normalized health/risk score.

    Args:
        predicted_rul: Predicted RUL values.

    Returns:
        Health score values aligned with predictions.

    Raises:
        NotImplementedError: Placeholder until scoring logic is implemented.
    """
    raise NotImplementedError("Health score calculation is not implemented yet.")


def detect_anomaly(features: pd.DataFrame) -> pd.Series:
    """Detect anomalous behavior in processed feature inputs.

    Args:
        features: Model input features.

    Returns:
        Boolean/int anomaly flags per observation.

    Raises:
        NotImplementedError: Placeholder until anomaly logic is implemented.
    """
    raise NotImplementedError("Anomaly detection is not implemented yet.")
