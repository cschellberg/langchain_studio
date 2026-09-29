from agent.graph import get_weather


def test_get_weather_includes_city_name() -> None:
    result = get_weather("San Francisco")
    assert "San Francisco" in result


def test_get_weather_returns_string() -> None:
    assert isinstance(get_weather("Tokyo"), str)
