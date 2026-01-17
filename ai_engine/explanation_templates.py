"""
Templates used to convert technical signals
into human-readable explanations.
"""

TEMPLATES = {
    "AMOUNT_ANOMALY": (
        "The transaction amount is significantly higher than "
        "the account’s normal spending behavior."
    ),

    "VELOCITY_SPIKE": (
        "Multiple transactions occurred within a short time frame, "
        "which may indicate automated or unauthorized activity."
    ),

    "GEO_ANOMALY": (
        "The transaction originated from a new geographic location "
        "not previously associated with this account."
    ),

    "BEHAVIOR_DRIFT": (
        "The transaction deviates from the account’s typical spending categories."
    ),

    "STRUCTURING": (
        "Multiple transactions were observed just below regulatory "
        "reporting thresholds, which may indicate structuring behavior."
    )
}
