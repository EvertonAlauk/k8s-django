import os

def test_app():
    assert "tests/test_app.py" in os.path.abspath(__file__)
