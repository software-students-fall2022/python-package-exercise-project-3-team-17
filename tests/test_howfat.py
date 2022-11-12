import random
import pytest
from src.amIFat.howfat import *

#---------------Calculation Tests with valid parameters----------------#
''' 
Valid parameter criteria:
        (1) Make sure howfat() returns a two-digit float BMI value and a message regarding obesity scale
        (2) Make sure age is an integer value
        (3) Make sure height (imperial and metric) is an integer value
            (3.1) Imperial height must be in inches, Metric height must be in cm
        (4) Make sure weight (imperial and metric) is an integer value
            (4.1) Imperial weight must be in pounds(lb), Metric weight must be in kg
        (5) Make sure scale is "m" or "i"
'''
def test_howfat_valid_metric():
    #metric arguments valid
    actual = howfat(25, 180, 67, "m")
    actual2 = howfat(24, 188, 72, "m")
    actual3 = howfat(41, 170, 92, "m")
    assert actual==(20.68,'You are healthy'), "howfat() did not return expected BMI"
    assert actual2==(20.37,'You are healthy'), "howfat() did not return expected BMI"
    assert actual3==(31.83,'You are obese'), "howfat() did not return expected BMI"

def test_howfat_valid_imperial():
    #imperial arguments valid
    actual = howfat(25,72, 190, "i")
    actual2 = howfat(34,70, 140, "i")
    actual3 = howfat(31, 71, 200, "i")
    assert actual==(25.77, 'You are overweight'), "howfat() did not return expected BMI"
    assert actual2==(20.09, 'You are healthy'), "howfat() did not return expected BMI"
    assert actual3==(27.89, 'You are overweight'), "howfat() did not return expected BMI"

def test_howfat_valid_ageScope():
    #valid arguments with age outside 18~65 group
    actual = howfat(5,40, 55, "i")
    actual2 = howfat(11,62, 80, "i")
    actual3 = howfat(81, 166, 44, "m")
    assert actual==('Please note that BMI for children, teens and seniors may not be accurate.', 24.17, 'You are healthy'), "howfat() did not return warning message for ages outside 18-65"
    assert actual2 ==('Please note that BMI for children, teens and seniors may not be accurate.', 14.63, 'You are underweight'), "howfat() did not return warning message for ages outside 18-65"
    assert actual3 ==('Please note that BMI for children, teens and seniors may not be accurate.', 15.97, 'You are underweight'), "howfat() did not return warning message for ages outside 18-65"

#--------------Invalid Arguments Exception Tests---------------------#
def test_howfat_invalid_parameters():
    with pytest.raises(Exception):
        #float value paramters
        howfat(25,171.5,55,"m")
        howfat(25,66.5,120,"i")
        howfat(34,173,109.2,"m")
        howfat(62,70.2,200, "i")
        #invalid scale paramter
        howfat(25,173,56, "j")
        #null param handling
        howfat(None,None,None,None)
        howfat(None,None,20,None)


#--------------Helper Function tests-------------------------------#
def test_valid_num():
    actual_int = valid_num(random.randint(1,100))
    actual_float = valid_num(15.5)
    actual_float2 = valid_num(490.44432)
    assert actual_int==(True), "integer validation error"
    assert actual_float ==(False), "integer validation error"
    assert actual_float2 ==(False), "integer validation error"


def test_valid_scale():
    actual_wrong_scale = valid_scale("j")
    actual_correct_scale1 = valid_scale("i")
    actual_correct_scale2 = valid_scale("m")
    assert actual_wrong_scale==(False), "scale parameter invalid"
    assert actual_correct_scale1 == (True), "scale parameter invalid"
    assert actual_correct_scale2 == (True), "scale parameter invalid"

def test_BMI_scale():
    actual_underweight =  BMI_scale(18.49)
    actual_healthy = BMI_scale(18.5)
    actual_overweight = BMI_scale(25)
    actual_obese= BMI_scale(30)
    assert actual_underweight==("You are underweight"), "obesity scale inaccurate"
    assert actual_healthy==("You are healthy"), "obesity scale inaccurate"
    assert actual_overweight==("You are overweight"), "obesity scale inaccurate"
    assert actual_obese==("You are obese"), "obesity scale inaccurate"