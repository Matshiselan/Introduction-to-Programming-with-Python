from hello import hello


def test_default():
    assert hello() == "Hello, World!"

def test_argunment():
    assert hello("Bob") == "Hello, Bob!"

