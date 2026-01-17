from risk_scoring.weights import SIGNAL_WEIGHTS, STRENGTH_MULTIPLIER


def calculate_risk_score(signals):
    """
    Calculates a cumulative risk score
    based on signal types and strengths.
    """

    total_score = 0
    contributing_factors = []

    for signal in signals:
        signal_type = signal["signal_type"]
        strength = signal["strength"]

        base_weight = SIGNAL_WEIGHTS.get(signal_type, 0)
        multiplier = STRENGTH_MULTIPLIER.get(strength, 1)

        score = base_weight * multiplier
        total_score += score

        contributing_factors.append({
            "signal_type": signal_type,
            "strength": strength,
            "score": score
        })

    return round(total_score, 2), contributing_factors
