def calculate_score(
    completed_modules,
    findings,
):
    """
    Calculate the SenseLab educational assessment score.
    """

    module_points = {
        "Reconnaissance": 15,
        "Network & DNS": 10,
        "HTTP Analysis": 15,
        "API Security": 15,
        "Vulnerability Lab": 20,
        "Risk Assessment": 10,
        "Remediation": 10,
        "Retesting": 5,
    }

    score = 0

    for module, points in module_points.items():

        if module in completed_modules:
            score += points

    return min(score, 100)
