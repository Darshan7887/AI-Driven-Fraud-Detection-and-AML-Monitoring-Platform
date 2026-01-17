import uuid
from datetime import datetime


def create_case(alert):
    """
    Groups alerts into a case for investigation.
    """

    case = {
        "case_id": str(uuid.uuid4()),
        "account_id": alert["account_id"],
        "created_at": datetime.utcnow().isoformat(),
        "alerts": [alert["alert_id"]],
        "status": "UNDER_REVIEW"
    }

    return case
