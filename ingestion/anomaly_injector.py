import random

def inject_anomalies(transactions):
    """
    Injects fraud & AML-like anomalies for testing.
    """

    if not transactions:
        return transactions

    # Amount spike anomaly
    spike_txn = random.choice(transactions)
    spike_txn["amount"] *= 8
    spike_txn["anomaly_type"] = "AMOUNT_SPIKE"

    # Velocity burst anomaly
    base_txn = random.choice(transactions)

    for i in range(3):
        transactions.append({
            **base_txn,
            "transaction_id": f"{base_txn['transaction_id']}_burst_{i}",
            "amount": round(base_txn["amount"] * 0.9, 2),
            "anomaly_type": "VELOCITY_SPIKE"
        })

    # Geographic anomaly
    geo_txn = random.choice(transactions)
    geo_txn["geo_country"] = "DE"
    geo_txn["anomaly_type"] = "GEO_ANOMALY"

    return transactions
