def detect_amount_anomaly(txn, account_profile):
    """
    Detects unusually high transaction amounts
    compared to account's historical average.
    """

    avg_amount = account_profile["avg_txn_amount"]
    txn_amount = txn["amount"]

    if txn_amount >= avg_amount * 5:
        return {
            "signal_type": "AMOUNT_ANOMALY",
            "strength": "HIGH",
            "reason": (
                f"Transaction amount {txn_amount} is significantly "
                f"higher than historical average {avg_amount}."
            )
        }

    if txn_amount >= avg_amount * 3:
        return {
            "signal_type": "AMOUNT_ANOMALY",
            "strength": "MEDIUM",
            "reason": (
                f"Transaction amount {txn_amount} is higher than "
                f"typical spending behavior."
            )
        }

    return None
