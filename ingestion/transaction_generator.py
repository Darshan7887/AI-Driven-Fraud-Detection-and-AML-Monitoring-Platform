import uuid
import random
from datetime import timedelta

def generate_transactions(profile, start_time, days=1):
    """
    Generates realistic transactions based on account behavior.
    """

    transactions = []
    current_time = start_time

    for _ in range(days * profile["txn_frequency_per_day"]):
        txn = {
            "transaction_id": str(uuid.uuid4()),
            "account_id": profile["account_id"],
            "timestamp": current_time.isoformat(),
            "amount": round(
                random.uniform(
                    profile["avg_txn_amount"] * 0.7,
                    profile["avg_txn_amount"] * 1.3
                ), 2
            ),
            "currency": "INR",
            "merchant_category": random.choice(
                profile["merchant_categories"]
            ),
            "geo_country": random.choice(
                profile["known_countries"]
            ),
            "channel": random.choice(["CARD", "UPI", "WALLET"]),
            "status": "SUCCESS"
        }

        transactions.append(txn)

        current_time += timedelta(
            minutes=random.randint(30, 180)
        )

    return transactions
