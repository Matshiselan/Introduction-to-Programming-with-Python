from basic import arithmetic_eval

def test_basic():
    assert arithmetic_eval("2 + 3") == 5
    assert arithmetic_eval("10 - 4") == 6
    assert arithmetic_eval("5 * 6") == 30
    assert arithmetic_eval("8 divide by 2") == 'Unsupported operation'
