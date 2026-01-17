from datetime import datetime


def generate_technical_report(account_id, signals, risk_score, priority):
    """
    Generates a detailed investigation report
    for fraud & risk teams.
    """

    report = {
        "account_id": account_id,
        "generated_at": datetime.utcnow().isoformat(),
        "risk_score": risk_score,
        "priority": priority,
        "signal_summary": [],
    }

    for signal in signals:
        report["signal_summary"].append({
            "signal_type": signal["signal_type"],
            "strength": signal["strength"],
            "reason": signal["reason"]
        })

    return report
