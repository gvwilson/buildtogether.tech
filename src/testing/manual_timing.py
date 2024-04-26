from datetime import datetime

def test_something():
    start = datetime.now()
    # …run the test…
    elapsed = datetime.now().microsecond - start.microsecond
