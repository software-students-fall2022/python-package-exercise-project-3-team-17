import pytest
import random 
from src.amIFat.calories import *
class Tests:

  

#------------------------------------calories() UNIT TESTS-----------------------------------
#--------------Valid input test for calories()-----------------
    ''' Valid input criteria:
        (1) Make sure calories() returns a valid caloric measurement 
        (2) Make sure calories() returns a positive integer
    '''
#Make sure calories() returns a valid caloric measurement 
def test_calories_with_valid_inputs():
    #Hand written calculations based off of verywellfit.com
    #age=22,gender="f", height=63, weight=120,activityLevel=3,scale="i"
    actual=calories(22,"f",63,120,2,"i")
    assert actual==1883, "calories() did not return the expected calories"


#Make sure calories() returns a positive integer-testing under the metric scale
def test_calories_with_valid_inputs_return_positive_number_metric():
    for i in range(10):
        #Test with scale=metric
        actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),random.randint(1,5),"m")
        assert type(actual)==int,"calories() did not return an integer under the metric scale"
        assert actual>0, "calories() did not return a positive value under the metric scale"

#Make sure calories() returns a positive integer-testing under the imperial scale
def test_calories_with_valid_inputs_return_positive_number_imperial():
    for i in range(10):
        #Test with scale=imperial
        actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(55,80),random.randint(80,400),random.randint(1,5),"i")
        assert type(actual)==int,"calories() did not return an integer under the imperial scale"
        assert actual>0, "calories() did not return a positive value under the imperial scale"
        
        

"""Criteria regarding invalid input for calories():
    *Note: "not accepted" means that calories() returns a value of -1
    (1) Make sure an age that falls out of the range of 1 and 120 is not accepted
    (2) Make sure age input other than an integer is not accepted 
    (3) Make sure inputs other than "f" and "m" for gender are not accepted
    (4) Make sure for height values other than numbers are not accepted 
    (4B) Make sure for weight values other than numbers are not accepted 
    (5) Make sure height outside the range 1 and 107 are not accepted (imperial)
    (5B) Make sure weight outside the range 1 and 1400 are not accepted (imperial)
    (6) Make sure height outside the range 1 and 272 are not accepted (metric)
    (6B) Make sure weight outside the range 1 and 635 are not accepted (metric)
    (7) Make sure inputs for scale other than "i" and "m" are not accepted
    (8) Make sure entries for activity levels that are not integers are not accepted
    (9) Make sure values for activity levels not within the range of 0 and 5 are not accepted
"""
#--------------Invalid input tests for calories()-----------------
#Make sure an age that falls out of the range of 1 and 120 is not accepted 
def test_calories_with_invalid_inputs_age_range():
    #Test with scale=metric 
    actual=calories(-1,random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),random.randint(1,5),"m")
    assert actual==-1,"Age less than 1 did not return -1"
    actual=calories(500,random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),random.randint(1,5),"m")
    assert actual==-1,"Age greater than 120 did not return -1"


#Make sure age input other than an integer is not accepted 
def test_calories_with_invalid_inputs_age_type():
    #Test with scale=metric
    #Test with a string input
    actual=calories("1",random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),random.randint(1,5),"m")
    assert actual==-1,"Input for age other than an integer (string) did not return -1"
    #Test with a float input
    actual=calories(10.5,random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),random.randint(1,5),"m")
    assert actual==-1,"Input for age other than an integer (float) did not return -1"


#Make sure inputs other than "f" and "m" for gender are not accepted
def test_calories_with_invalid_inputs_gender():
    #Test with scale=metric 
    #Put "female" instead of f or m
    actual=calories(random.randint(18,100),"female",
        random.randint(150,195),random.randint(45,100),random.randint(1,5),"m")
    assert actual==-1, "An invalid value (inserted random string) for gender did not return -1"
    #Put 100 instead of f or m
    actual=calories(random.randint(18,100),100,
        random.randint(150,195),random.randint(45,100),random.randint(1,5),"m")
    assert actual==-1, "An invalid value (inserted an integer) for gender did not return -1"


#Make sure for height values other than numbers are not accepted 
def test_calories_with_invalid_inputs_height_type():
    #Test with scale=metric 
    #Put a string in for height
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        "height",random.randint(45,100),random.randint(1,5),"m")
    assert actual==-1,"A non numeric value for height did not return -1"
    

#Make sure for weight values other than numbers are not accepted 
def test_calories_with_invalid_inputs_weight_type():
    #Test with scale=metric 
    #Put a string in for weight
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),"weight",random.randint(1,5),"m")
    assert actual==-1, "A non numeric value for weight did not return -1"


#Make sure height outside the range 1 and 107 are not accepted (imperial)
def test_calories_with_invalid_inputs_height_ranges_imperial():
    #Test with scale=imperial 
    #height below 1
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        -100,random.randint(80,350),random.randint(1,5),"i")
    assert actual==-1,"A value less than 1 for height did not return -1 (imperial)"
    #height above 107
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        200,random.randint(80,350),random.randint(1,5),"i")
    assert actual==-1,"A value above 107 for height did not return -1 (imperial)"


#Make sure weight outside the range 1 and 1400 are not accepted (imperial)
def test_calories_with_invalid_inputs_weight_ranges_imperial():
     #Test with scale=imperial 
    #weight below 1
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(55,75),-100,random.randint(1,5),"i")
    assert actual==-1, "A value less than 1 for weight did not return -1 (imperial)"
     #weight above 1400
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(55,75),7000,random.randint(1,5),"i")
    assert actual==-1, "A value above 1400 for weight did not return -1 (imperial)"


#Make sure height outside the range 1 and 272 are not accepted (metric)
def test_calories_with_invalid_inputs_height_ranges_metric():
    #Test with scale=metric 
    #height below 1
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        -100,random.randint(45,100),random.randint(1,5),"m")
    assert actual==-1,"A value less than 1 for height did not return -1 (metric)"
    #height above 272
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        500,random.randint(45,100),random.randint(1,5),"m")
    assert actual==-1,"A value above 272 for height did not return -1 (metric)"


#Make sure weight outside the range 1 and 635 are not accepted (metric)
def test_calories_with_invalid_inputs_weight_ranges_metric():
    #Test with scale=metric 
     #weight below 1
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),-100,random.randint(1,5),"m")
    assert actual==-1, "A value less than 1 for weight did not return -1 (metric)"
    #weight above 635
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),1000,random.randint(1,5),"m")
    assert actual==-1, "A value above 635 for weight did not return -1 (metric)"


#Make sure inputs for scale other than "i" and "m" are not accepted
def test_calories_with_invalid_inputs_scale():
    #Test with scale=metric 
    #Input "metric"
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),random.randint(1,5),"metric")
    assert actual==-1,"An invalid input for scale (random string) did not return -1"
    #Input a number 
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),random.randint(1,5),100)
    assert actual==-1,"An invalid input for scale (a number) did not return -1"


#Make sure entries for activity levels that are not integers are not accepted
def test_calories_with_invalid_inputs_activityLevel_integer():
    #Test with scale=metric
    #Test non-integer
    #Use a float as an entry
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),10.5,"m")
    assert actual==-1, "A non-integer (float) for activityLevel did not return -1"
     #Use a string as an entry
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),"activityLevel","m")
    assert actual==-1, "A non-integer (string) for activityLevel did not return -1"


#Make sure values for activity levels not within the range of 0 and 5 are not accepted
def test_calories_with_invalid_inputs_activityLevel_range():
    #Test with scale=metric
    #activityLevel below 0
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),-1,"m")
    assert actual==-1, "A value below 0 for activityLevel did not return -1"

    #activityLevel above 5
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),10,"m")
    assert actual==-1, "A value above 5 for activityLevel did not return -1"
    


#-------------------------------Helper function- convertScale() UNIT TESTS-----------------------------------
'''
Valid input criteria:
(1) Make sure the expected measurements are returned
(2) Make sure return values are positive
(3) Make sure return values are floats
'''    

#Make sure the expected measurements are returned
def test_convertScale():
    #Compare to hand calculated values
    actual1,actual2=convertScale(63,120)
    assert actual1==160.02, "convertScale() did not return the expected height"
    assert actual2==54.4310844, "convertScale() did not return the expected weight"


#Make sure return values are floats
def test_convertScale_return_type():
    actual1, actual2=convertScale(random.randint(55,72),random.randint(80,350))
    assert type(actual1)==float, "convertScale() did not return a numeric height"
    assert type(actual2)==float, "convertScale() did not return a numeric weight"


#Make sure return values are positive
def test_convertScale_return_positive():
    actual1, actual2=convertScale(random.randint(55,72),random.randint(80,350))
    assert actual1>0, "convertScale() did not return a positive height"
    assert actual2>0, "convertScale() did not return a positive weight"



'''
Invalid input criteria:
*Note: "not accepted" means that convertScale() returns a value of -1
(1) Make sure height out of range 1-107 are not accepted
(2) Make sure weight out of range of 1-1400 are not accepted
(3) Make sure inputs other than numbers are not accepted for height
(3B) Make sure inputs other than numbers are not accepted for weight
'''  

#--------------Invalid input tests for convertScale()-----------------

#Make sure inputs other than numbers are not accepted for height
def test_convertScale_with_invalid_inputs_height_type():
    #Test with string
    actual1, actual2=convertScale("1",random.randint(80,350))
    assert actual1==-1, "Invalid height input (string) did not return a -1 for height"
    assert actual2==-1, "Invalid height input (string) did not return a -1 for weight"


#Make sure inputs other than numbers are not accepted for weight
def test_convertScale_with_invalid_inputs_weight_type():
    actual1, actual2=convertScale(random.randint(55,72),"200")
    assert actual1==-1, "Invalid weight input (string) did not return a -1 for height"
    assert actual2==-1, "Invalid weight input (string) did not return a -1 for weight"


#Make sure height out of range 1-107 are not accepted
def test_convertScale_with_invalid_inputs_height():
    #height<1
    actual1, actual2=convertScale(-1,random.randint(80,350))
    assert actual1==-1, "Height less than 1 did not return a -1 for height"
    assert actual2==-1, "Height less than 1 did not return a -1 for weight"
    #height>107
    actual1, actual2=convertScale(500,random.randint(80,350))
    assert actual1==-1, "Height greater than 107 did not return a -1 for height"
    assert actual2==-1, "Height greater than 107 did not return a -1 for weight"


#Make sure weight out of range of 1-1400 are not accepted
def test_convertScale_with_invalid_inputs_height():
    #weight<1
    actual1, actual2=convertScale(random.randint(55,72),-1)
    assert actual1==-1, "Weight less than 1 did not return a -1 for height"
    assert actual2==-1, "Weight less than 1 did not return a -1 for weight"
    #weight>1400
    actual1, actual2=convertScale(random.randint(55,72),2000)
    assert actual1==-1, "Weight greater than 1400 did not return a -1 for height"
    assert actual2==-1, "Weight greater than 1400 did not return a -1 for weight"




    
    