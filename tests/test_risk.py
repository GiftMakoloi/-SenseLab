from engine.risk import calculate_risk


def test_critical_risk():

    result = calculate_risk(
        5,
        5,
        5,
    )

    assert result["score"] == 100
    assert result["level"] == "CRITICAL"


def test_low_risk():

    result = calculate_risk(
        1,
        1,
        1,
    )

    assert result["score"] == 1
    assert result["level"] == "LOW"


def test_risk_range():

    result = calculate_risk(
        3,
        4,
        2,
    )

    assert 0 <= result["score"] <= 100
