import os

def test_app():
    assert os.path.abspath(__file__) == "/usr/src/app/tests/test_app.py"
