# PREDIX Architecture

PREDIX is structured as a modular pipeline-oriented project to support incremental implementation by multiple contributors.

## Pipeline 1: Data Pipeline

Raw data → validation → cleaning/preprocessing → feature engineering → processed data.

- `src/data/load_data.py`: load raw datasets and validate schema/quality.
- `src/data/preprocess.py`: clean and normalize validated inputs.
- `src/features/engineering.py`: create model-ready features.

## Pipeline 2: RUL Prediction Pipeline

Processed sensor data → feature extraction/input preparation → ML model → RUL prediction → health/risk score.

- `src/models/train.py`: train RUL models.
- `src/models/predict.py`: predict RUL, calculate health score, detect anomalies.
- `src/models/evaluate.py`: evaluate model quality.

## Pipeline 3: Maintenance Decision Pipeline

RUL + health score + anomaly information → risk assessment → maintenance priority → recommended maintenance action.

- `src/decision/maintenance.py`: assess risk and generate recommendations.

## Pipeline 4: Fleet Availability Pipeline

Aircraft/component health states → risk ranking → maintenance prioritisation → fleet availability/readiness metrics.

- `src/decision/maintenance.py`: fleet-level readiness calculation.

## Application Layer

- `app/streamlit_app.py` is the initial UI entrypoint. It currently provides a project placeholder and will later integrate all four pipelines.
