import csv
from datetime import datetime
from behavior_profiles import generate_account_profile
from transaction_generator import generate_transactions
from anomaly_injector import inject_anomalies

def run_batch_ingestion():
    profile = generate_account_profile("ACC_1001")
    start_time = datetime.now()

    transactions = generate_transactions(
        profile,
        start_time,
        days=1
    )

    transactions = inject_anomalies(transactions)

    with open("../data/transactions.csv", "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=transactions[0].keys()
        )
        writer.writeheader()
        writer.writerows(transactions)

    print(f"[INFO] Ingested {len(transactions)} transactions")

if __name__ == "__main__":
    run_batch_ingestion()
