from src.amIFat.macros import *
import pytest
import math

def test_calculateREE():
    assert calculateREE(21, 'm', 175, 80, 'm') == 1793.75

def test_raiseExceptionGenderREE():
     with pytest.raises(Exception):
        calculateREE(45, 'x', 123, 78, 'm')

def test_raiseExceptionScaleREE():
         with pytest.raises(Exception):
            calculateREE(12, 'm', 571, 345678, 'x')

def test_validDimensions():
    with pytest.raises(Exception):
        validDimensions(21, 21, 1401)
    with pytest.raises(Exception):
        validDimensions(282, 21, 21)
    with pytest.raises(Exception):
        validDimensions(150, 1500, 21)

def test_calculateTDEE():
    ree = calculateREE(29, 'm', 183, 88, 'm')
    assert math.ceil(calculateTDEE(ree, 4)) == 3250

# def test_raiseExceptionTDEE():
#     with pytest.raises(Exception):
#         calculateTDEE(68, )
