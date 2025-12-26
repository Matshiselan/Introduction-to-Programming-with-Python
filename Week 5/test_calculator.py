from calculator import square
import pytest

# def main():
#     test_square()


    # try:
    #     assert square(3) == 9
    #     assert square(-4) == 16
    # except AssertionError:
    #     print("Test failed.")
    #     raise

# if __name__ == "__main__":
#     main()
#     print("All tests passed.")


def test_positive():
    assert square(3) == 9
    assert square(5) == 25

def test_negative():
    assert square(-4) == 16
    assert square(-1) == 1

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("a")