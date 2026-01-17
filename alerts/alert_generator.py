import uuid
from datetime import datetime


def generate_alert(account_id, risk_score, priority, signals):
    """
    Generates a fraud alert based on risk assessment.
    """

    alert = {
        "alert_id": str(uuid.uuid4()),
        "account_id": account_id,
        "created_at": datetime.utcnow().isoformat(),
        "risk_score": risk_score,
        "priority": priority,
        "signal_count": len(signals),
        "status": "NEW"
    }

    return alert
