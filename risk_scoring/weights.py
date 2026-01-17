"""
Risk weights are typically owned by
Fraud Strategy / Risk Governance teams.
"""

SIGNAL_WEIGHTS = {
    "AMOUNT_ANOMALY": 30,
    "VELOCITY_SPIKE": 25,
    "GEO_ANOMALY": 30,
    "BEHAVIOR_DRIFT": 15,
    "STRUCTURING": 35
}

STRENGTH_MULTIPLIER = {
    "LOW": 0.5,
    "MEDIUM": 1.0,
    "HIGH": 1.5
}
