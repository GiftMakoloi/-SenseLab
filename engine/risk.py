def calculate_risk(
    likelihood,
    impact,
    exploitability,
):
    """
    SenseLab educational risk model.

    Inputs are expected to be values between 1 and 5.
    """

    likelihood = max(1, min(5, likelihood))
    impact = max(1, min(5, impact))
    exploitability = max(1, min(5, exploitability))

    raw_score = (
        likelihood
        * impact
        * exploitability
    )

    score = round(
        (raw_score / 125) * 100
    )

    if score >= 80:
        level = "CRITICAL"
    elif score >= 60:
        level = "HIGH"
    elif score >= 40:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "score": score,
        "level": level,
    }
