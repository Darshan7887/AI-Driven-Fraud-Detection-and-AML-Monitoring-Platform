def assign_priority(risk_score):
    """
    Converts numeric risk score
    into analyst-friendly priority.
    """

    if risk_score >= 70:
        return "HIGH"
    elif risk_score >= 35:
        return "MEDIUM"
    else:
        return "LOW"
