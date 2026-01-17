import csv

from ingestion.behavior_profiles import generate_account_profile
from detection.amount_rules import detect_amount_anomaly
from detection.geo_rules import detect_geo_anomaly
from detection.behavior_rules import detect_behavior_drift
from detection.velocity_rules import detect_velocity_spike
from detection.structuring_rules import detect_structuring


def run_detection():
    with open("data/transactions.csv") as f:
        transactions = list(csv.DictReader(f))

    # Convert numeric fields
    for txn in transactions:
        txn["amount"] = float(txn["amount"])

    account_profile = generate_account_profile(
        transactions[0]["account_id"]
    )

    all_signals = []

    # Per-transaction detection
    for txn in transactions:
        for detector in [
            detect_amount_anomaly,
            detect_geo_anomaly,
            detect_behavior_drift
        ]:
            signal = detector(txn, account_profile)
            if signal:
                signal.update({
                    "transaction_id": txn["transaction_id"],
                    "account_id": txn["account_id"]
                })
                all_signals.append(signal)

    # Cross-transaction detection
    all_signals.extend(detect_velocity_spike(transactions))
    all_signals.extend(detect_structuring(transactions))

    print("\n=== DETECTED RISK SIGNALS ===")
    for signal in all_signals:
        print(signal)


if __name__ == "__main__":
    run_detection()
