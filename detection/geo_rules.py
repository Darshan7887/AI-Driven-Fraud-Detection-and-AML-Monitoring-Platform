def detect_geo_anomaly(txn, account_profile):
    """
    Detects transactions from new or unusual geographies.
    """

    country = txn["geo_country"]
    known_countries = account_profile["known_countries"]

    if country not in known_countries:
        return {
            "signal_type": "GEO_ANOMALY",
            "strength": "HIGH",
            "reason": (
                f"Transaction originated from new country {country}, "
                f"not previously associated with this account."
            )
        }

    return None
