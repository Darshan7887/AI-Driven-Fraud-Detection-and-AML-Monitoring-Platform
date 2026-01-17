import random

def generate_account_profile(account_id: str):
    """
    Defines normal spending behavior for an account.
    Acts as baseline for fraud & AML detection.
    """

    avg_amount = random.randint(500, 3000)
    txn_frequency_per_day = random.randint(2, 6)

    profile = {
        "account_id": account_id,
        "avg_txn_amount": avg_amount,
        "txn_frequency_per_day": txn_frequency_per_day,
        "known_countries": ["IN"],
        "merchant_categories": [
            "GROCERY",
            "FOOD",
            "FUEL",
            "UTILITIES",
            "ECOMMERCE"
        ]
    }

    return profile
