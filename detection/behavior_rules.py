def detect_behavior_drift(txn, account_profile):
    """
    Detects spending in merchant categories
    not typical for the account.
    """

    category = txn["merchant_category"]
    known_categories = account_profile["merchant_categories"]

    if category not in known_categories:
        return {
            "signal_type": "BEHAVIOR_DRIFT",
            "strength": "MEDIUM",
            "reason": (
                f"Merchant category {category} deviates "
                f"from historical spending behavior."
            )
        }

    return None
