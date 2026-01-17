from datetime import datetime


def generate_executive_report(account_id, risk_score, priority):
    """
    Generates a concise executive-level summary.
    """

    summary = {
        "account_id": account_id,
        "generated_at": datetime.utcnow().isoformat(),
        "overview": (
            f"An account was flagged as {priority} risk "
            f"with an overall risk score of {risk_score}. "
            "The activity exhibited patterns inconsistent "
            "with historical behavior and warrants review."
        )
    }

    return summary
