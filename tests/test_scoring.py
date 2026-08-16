from engine.scoring import calculate_score


def test_empty_score():

    score = calculate_score(
        set(),
        [],
    )

    assert score == 0


def test_completed_modules_score():

    modules = {
        "Reconnaissance",
        "HTTP Analysis",
        "API Security",
    }

    score = calculate_score(
        modules,
        [],
    )

    assert score == 45


def test_score_never_exceeds_100():

    modules = {
        "Reconnaissance",
        "Network & DNS",
        "HTTP Analysis",
        "API Security",
        "Vulnerability Lab",
        "Risk Assessment",
        "Remediation",
        "Retesting",
    }

    score = calculate_score(
        modules,
        [],
    )

    assert score <= 100
