from ai_engine.explanation_templates import TEMPLATES

def generate_signal_explanations(signals):
    """
    Converts signals into human-readable explanations.
    """

    explanations = []

    for signal in signals:
        template = TEMPLATES.get(
            signal["signal_type"],
            "Unusual activity was detected on this account."
        )
        explanations.append(template)

    return explanations


def generate_analyst_summary(explanations):
    """
    Produces an analyst-focused explanation.
    """

    unique_points = list(set(explanations))

    summary = "This account was flagged due to the following risk indicators:\n"
    for point in unique_points:
        summary += f"- {point}\n"

    return summary


def generate_executive_summary(risk_score, priority):
    """
    Produces an executive-friendly summary.
    """

    return (
        f"The system identified high-risk transactional behavior "
        f"with an overall risk score of {risk_score} "
        f"and a priority level of {priority}. "
        f"Further investigation is recommended."
    )
