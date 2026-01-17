def review_case(case, decision):
    """
    Simulates analyst review decision.
    """

    if decision == "ESCALATE":
        case["status"] = "ESCALATED"
        case["resolution"] = "Referred for further investigation"

    elif decision == "CLOSE_FALSE_POSITIVE":
        case["status"] = "CLOSED"
        case["resolution"] = "False positive"

    elif decision == "CONFIRMED_FRAUD":
        case["status"] = "CLOSED"
        case["resolution"] = "Fraud confirmed and mitigated"

    else:
        case["status"] = "UNDER_REVIEW"

    return case
