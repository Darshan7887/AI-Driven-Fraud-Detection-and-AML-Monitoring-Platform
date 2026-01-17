def detect_structuring(transactions, threshold=10000):
    """
    Detects repeated transactions just below reporting thresholds.
    """

    signals = []
    near_threshold = [
        txn for txn in transactions
        if threshold * 0.8 <= txn["amount"] < threshold
    ]

    if len(near_threshold) >= 3:
        signals.append({
            "signal_type": "STRUCTURING",
            "strength": "HIGH",
            "reason": (
                f"Multiple transactions detected just below "
                f"the reporting threshold of {threshold}."
            )
        })

    return signals
