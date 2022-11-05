from macros import *

def test_calculateREE():
    # print(10 * 80 + 6.25 * 175 - 5 * 21 + 5)
    # print(calculateREE(21, 'm', 175, 80, 'm'))
    assert calculateREE(21, 'm', 175, 80, 'm') == 1793.75