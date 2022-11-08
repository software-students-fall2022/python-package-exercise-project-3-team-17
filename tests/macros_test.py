from src.amIFat.macros import *
import pytest
import math

#macros
def test_macrosInvalidScale():
    with pytest.raises(Exception):
        macros(50, 50, 'v')

def test_macrosReturnType():
    actual = macros(50, 80, 'i')
    assert isinstance(actual, dict)

def test_macros():
    actual = macros(80, 3000000, 'i')
    expected = {
        'Protein Intake': 66.0, 
        'Fat Intake': 83333.33333333333, 
        'Carb Intake': 562434.0
    }
    assert actual == expected
    actualImperial = macros(36.2811791383, 3000000, 'm')
    for i in actualImperial:
        actualImperial[i] = math.ceil(actualImperial[i])
    for i in actual:
        actual[i] = math.ceil(actual[i])
    assert actual == actualImperial

#calculateREE
def test_calculateREE():
    actual = calculateREE(21, 'm', 175, 80, 'm')
    actual2 = calculateREE(21, 'm', 68.8976, 176.37, 'i')
    assert actual == 1793.75
    assert math.ceil(actual2) == math.ceil(actual)

def test_raiseExceptionGenderREE():
     with pytest.raises(Exception):
        calculateREE(45, 'x', 123, 78, 'm')

def test_raiseExceptionScaleREE():
         with pytest.raises(Exception):
            calculateREE(12, 'm', 571, 345678, 'x')

#helper function
def test_validDimensionsException():
    with pytest.raises(Exception):
        validDimensions(21, 21, 1401)
    with pytest.raises(Exception):
        validDimensions(282, 21, 21)
    with pytest.raises(Exception):
        validDimensions(150, 1500, 21)

def test_validDimensionsEmptyParams():
    actual = validDimensions()
    assert actual == validDimensions(1,1,1)

def test_validDimensionsCorrectParams():
    actual = validDimensions(21, 21, 21)
    assert actual == True

#calculateTDEE
def test_calculateTDEE():
    ree = calculateREE(29, 'm', 183, 88, 'm')
    actual = math.ceil(calculateTDEE(ree, 4))
    assert actual == 3250

def test_calculateTDEEInvalidActivityLevel():
    with pytest.raises(Exception):
        calculateTDEE(10, 5)
    with pytest.raises(Exception):
        calculateTDEE(10, 0)

def test_calculateTDEEDefaultEnergyLvl():
    actual = calculateTDEE(87)
    assert actual == calculateTDEE(87, 2)

#weightLossOrGainCalculator
def test_weightLossOrGainCalculatorInvalidAimException():
    with pytest.raises(Exception):
        weightLossOrGainCalculator(54, 'b')

def test_weightLossOrGainCalculator():
    actual = weightLossOrGainCalculator(50, 'g')
    actual2 = weightLossOrGainCalculator(99, 'l')
    assert actual == 60.0
    assert actual2 == 79.2

def test_weightLossOrGainCalculatorDefault():
    actual = weightLossOrGainCalculator(50, 'l')
    actual2 = weightLossOrGainCalculator(50)
    assert actual == actual2
