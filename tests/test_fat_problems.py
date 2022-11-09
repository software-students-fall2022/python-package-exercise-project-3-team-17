from amIFat.fat_problems import *
import random
import pytest

diseases_list = [
    '',
    'diabetes',                     #1
    'hypertension',                 #2
    'CVD',                          #3
    'heart disease',                #4
    'stroke',                       #5
    'gallbladder disease',          #6
    'osteoarthritis',               #7
    'sleep apnea',                  #8
    'breathing problems',           #9
    'cancer',                       #10
    'depression',                   #11
    'anxiety',                      #12
    'mental disorders',             #13
    'body pain',                    #14
    'flatty lever diseases',        #15
    'metabolic syndrome',           #16
    'eye diseases',                 #17
    'kidney diseases',              #18
    'malnutrition',                 #19
    'osteoporosis',                 #20
    'decreased muscle strength',    #21
    'hypothermia' ,                 #22
    'lowered immunity'              #23
]

levels_list = [
    '',
    'low',              #1
    'medium',           #2
    'increased',        #3
    'high',             #4
    'very high',        #5
    'extremely high'    #6
]

#---------------Calculation Tests with valid parameters----------------#
def test_output_type():
    outputs = []
    outputs.append(fat_problems(13.0))
    outputs.append(fat_problems(16.0))
    outputs.append(fat_problems(19.0))
    outputs.append(fat_problems(27.0))
    outputs.append(fat_problems(37.0))
    outputs.append(fat_problems(47.0))
    for output in outputs:
        assert type(output) is dict
        for disease_risk in output:
            assert type(disease_risk) is str
            assert disease_risk in diseases_list
            assert type(output[disease_risk]) is str            
            assert output[disease_risk] in levels_list

#--------------Invalid Arguments Exception Tests---------------------#
def test_fat_problems_invalid_parameters():
    with pytest.raises(Exception):
        fat_problems(-1.0)
        fat_problems("bmi")
        fat_problems(5.0)
        fat_problems(55.0)
        fat_problems(None)
