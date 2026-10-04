# PREDIX

AI-powered predictive maintenance and fleet availability platform for SIH 2026 Problem Statement 26249.

## Project Overview

PREDIX is a modular prototype focused on improving aircraft maintenance planning and fleet readiness through data-driven risk assessment.

## Problem Statement

**SIH 2026 Problem Statement 26249:**
"Air Power – Predictive Maintenance & Fleet Availability."

Aircraft maintenance data is often fragmented across health-monitoring systems, technical records, spare inventories, and maintenance agencies, leading to reactive maintenance and avoidable downtime.

## Proposed Solution

PREDIX will integrate aircraft health, maintenance, and logistics signals to:

- predict component degradation trends
- estimate Remaining Useful Life (RUL)
- detect anomalies and emerging risk
- recommend maintenance actions and priority
- provide fleet-level availability/readiness metrics

## Architecture Overview

The repository is organized into four connected pipelines:

1. **Data Pipeline**: raw data ingestion, validation, cleaning, preprocessing, and feature engineering.
2. **RUL Prediction Pipeline**: processed data to RUL predictions and health/risk scoring.
3. **Maintenance Decision Pipeline**: risk assessment and maintenance recommendation generation.
4. **Fleet Availability Pipeline**: risk ranking and fleet readiness/availability metrics.

See `/docs/architecture.md` for details.

## Data Strategy

- NASA C-MAPSS is the public source for aerospace degradation/RUL modelling.
- Prototype aircraft health, maintenance, and inventory datasets are synthetic.
- The prototype does **not** assume access to classified or operational defence data.

See `/docs/data.md` for details.

## Planned Technology Stack

- Python
- pandas, numpy
- scikit-learn, xgboost, lightgbm
- streamlit
- plotly
- joblib

## Current Project Status

🚧 Initial clean architecture skeleton is set up.

### Not Implemented Yet

- Final ML model training logic and tuned algorithms
- Production decision heuristics/business rules
- Full dashboard workflows and visual analytics
- LLM agent capabilities
- Production-readiness hardening
