"""Streamlit entrypoint for the PREDIX prototype."""

import streamlit as st


def main() -> None:
    """Render the current PREDIX prototype landing page."""
    st.title("PREDIX")
    st.subheader("AI-Powered Predictive Maintenance & Fleet Availability")

    st.markdown("## Planned Module Integration")
    st.markdown("- Data pipeline module (ingestion, validation, preprocessing)")
    st.markdown("- RUL prediction module (model training and inference)")
    st.markdown("- Maintenance decision module (risk and recommendations)")
    st.markdown("- Fleet availability module (readiness and prioritisation metrics)")


if __name__ == "__main__":
    main()
