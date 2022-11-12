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
#Test with imperial scale
def test_calories_with_valid_inputs_imperial():
    #Hand written calculations based off of verywellfit.com
    #age=22,gender="f", height=63, weight=120,activityLevel=2,scale="i"
    actual=calories(22,"f",63,120,2,"i")
    assert actual==1883, "calories() did not return the expected calories (1883)"
    #age=30,gender="m", height=70, weight=150,activityLevel=3,scale="i"
    actual=calories(30,"m",70,150,3,"i")
    assert actual==2618, "calories() did not return the expected calories (2618)"
#Test with metric scale
def test_calories_with_valid_inputs_metric():
    #age=28,gender="f", height=155, weight=40,activityLevel=5,scale="m"
    actual=calories(28,"f",155,40,5,"m")
    assert actual==2268, "calories() did not return the expected calories (2268)"
    #age=18,gender="m", height=190, weight=75,activityLevel=4,scale="m"
    actual=calories(18,"m",190,75,4,"m")
    assert actual==3324, "calories() did not return the expected calories (3324)"

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
#Test below range
def test_calories_with_invalid_inputs_age_range_below():
    #Test with scale=metric 
    actual=calories(-1,random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),random.randint(1,5),"m")
    assert actual==-1,"Age less than 1 did not return -1"
#Test above range
def test_calories_with_invalid_inputs_age_range_above():
    actual=calories(500,random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),random.randint(1,5),"m")
    assert actual==-1,"Age greater than 120 did not return -1"
    

#Make sure age input other than an integer is not accepted 
#Test with string input
def test_calories_with_invalid_inputs_age_type_withString():
    #Test with scale=metric
    #Test with a string input
    actual=calories("1",random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),random.randint(1,5),"m")
    assert actual==-1,"Input for age other than an integer (string) did not return -1"
#Test with float input
def test_calories_with_invalid_inputs_age_type_withFloat():
    #Test with a float input
    actual=calories(10.5,random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),random.randint(1,5),"m")
    assert actual==-1,"Input for age other than an integer (float) did not return -1"


#Make sure inputs other than "f" and "m" for gender are not accepted
#Test with random string input
def test_calories_with_invalid_inputs_gender_randomString():
    #Test with scale=metric 
    #Put "female" instead of f or m
    actual=calories(random.randint(18,100),"female",
        random.randint(150,195),random.randint(45,100),random.randint(1,5),"m")
    assert actual==-1, "An invalid value (inserted random string) for gender did not return -1"
#Test with an integer input
def test_calories_with_invalid_inputs_gender_integer():
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
#Test below range
def test_calories_with_invalid_inputs_height_ranges_imperial_below():
    #Test with scale=imperial 
    #height below 1
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        -100,random.randint(80,350),random.randint(1,5),"i")
    assert actual==-1,"A value less than 1 for height did not return -1 (imperial)"
#Test above range
def test_calories_with_invalid_inputs_height_ranges_imperial_above():
    #height above 107
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        200,random.randint(80,350),random.randint(1,5),"i")
    assert actual==-1,"A value above 107 for height did not return -1 (imperial)"


#Make sure weight outside the range 1 and 1400 are not accepted (imperial)
#Test below range
def test_calories_with_invalid_inputs_weight_ranges_imperial_below():
     #Test with scale=imperial 
    #weight below 1
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(55,75),-100,random.randint(1,5),"i")
    assert actual==-1, "A value less than 1 for weight did not return -1 (imperial)"
def test_calories_with_invalid_inputs_weight_ranges_imperial_above():
      #weight above 1400
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(55,75),7000,random.randint(1,5),"i")
    assert actual==-1, "A value above 1400 for weight did not return -1 (imperial)"


#Make sure height outside the range 1 and 272 are not accepted (metric)
#Test below range
def test_calories_with_invalid_inputs_height_ranges_metric_below():
    #Test with scale=metric 
    #height below 1
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        -100,random.randint(45,100),random.randint(1,5),"m")
    assert actual==-1,"A value less than 1 for height did not return -1 (metric)"
#Test above range
def test_calories_with_invalid_inputs_height_ranges_metric_above():
    #height above 272
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        500,random.randint(45,100),random.randint(1,5),"m")
    assert actual==-1,"A value above 272 for height did not return -1 (metric)"

#Make sure weight outside the range 1 and 635 are not accepted (metric)
#Test below range
def test_calories_with_invalid_inputs_weight_ranges_metric_below():
    #Test with scale=metric 
     #weight below 1
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),-100,random.randint(1,5),"m")
    assert actual==-1, "A value less than 1 for weight did not return -1 (metric)"
#Test above range
def test_calories_with_invalid_inputs_weight_ranges_metric_above():
    #weight above 635
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),1000,random.randint(1,5),"m")
    assert actual==-1, "A value above 635 for weight did not return -1 (metric)"


#Make sure inputs for scale other than "i" and "m" are not accepted
#Test with a random string
def test_calories_with_invalid_inputs_scale_withString():
    #Test with scale=metric 
    #Input "metric"
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),random.randint(1,5),"metric")
    assert actual==-1,"An invalid input for scale (random string) did not return -1"
#Test with a number input
def test_calories_with_invalid_inputs_scale_withNum():
    #Input a number 
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),random.randint(1,5),100)
    assert actual==-1,"An invalid input for scale (a number) did not return -1"


#Make sure entries for activity levels that are not integers are not accepted
#Test with a float input
def test_calories_with_invalid_inputs_activityLevel_integer_withFloat():
    #Test with scale=metric
    #Test non-integer
    #Use a float as an entry
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),10.5,"m")
    assert actual==-1, "A non-integer (float) for activityLevel did not return -1"
#Test with a string input
def test_calories_with_invalid_inputs_activityLevel_integer_withString():
     #Use a string as an entry
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),"activityLevel","m")
    assert actual==-1, "A non-integer (string) for activityLevel did not return -1"


#Make sure values for activity levels not within the range of 0 and 5 are not accepted
#Test below 0
def test_calories_with_invalid_inputs_activityLevel_range_below():
    #Test with scale=metric
    #activityLevel below 0
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),-1,"m")
    assert actual==-1, "A value below 0 for activityLevel did not return -1"
#Test above 5
def test_calories_with_invalid_inputs_activityLevel_range_above():
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
    #height=62, weight=120
    actual1,actual2=convertScale(63,120)
    assert actual1==160.02, "convertScale() did not return the expected height (160.02)"
    assert actual2==54.4310844, "convertScale() did not return the expected weight (54.4310844)"
    #height=55, weight=80
    actual1,actual2=convertScale(55,80)
    assert actual1==139.7, "convertScale() did not return the expected height (139.7)"
    assert actual2==36.2873896, "convertScale() did not return the expected weight (36.2873896)"
    #height=90, weight=200
    actual1,actual2=convertScale(90,200)
    assert actual1==228.6, "convertScale() did not return the expected height (228.6)"
    assert actual2==90.718474, "convertScale() did not return the expected weight (90.718474)"
    #height=71, weight=300
    actual1,actual2=convertScale(71,300)
    assert actual1==180.34, "convertScale() did not return the expected height (180.34)"
    assert actual2==136.077711, "convertScale() did not return the expected weight (136.077711)"




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
#Test below range
def test_convertScale_with_invalid_inputs_height_below():
    #height<1
    actual1, actual2=convertScale(-1,random.randint(80,350))
    assert actual1==-1, "Height less than 1 did not return a -1 for height"
    assert actual2==-1, "Height less than 1 did not return a -1 for weight"
#Test above range
def test_convertScale_with_invalid_inputs_height_above():
    #height>107
    actual1, actual2=convertScale(500,random.randint(80,350))
    assert actual1==-1, "Height greater than 107 did not return a -1 for height"
    assert actual2==-1, "Height greater than 107 did not return a -1 for weight"


#Make sure weight out of range of 1-1400 are not accepted
#Test below range
def test_convertScale_with_invalid_inputs_height_below():
    #weight<1
    actual1, actual2=convertScale(random.randint(55,72),-1)
    assert actual1==-1, "Weight less than 1 did not return a -1 for height"
    assert actual2==-1, "Weight less than 1 did not return a -1 for weight"
#Test above range
def test_convertScale_with_invalid_inputs_height_above():
    #weight>1400
    actual1, actual2=convertScale(random.randint(55,72),2000)
    assert actual1==-1, "Weight greater than 1400 did not return a -1 for height"
    assert actual2==-1, "Weight greater than 1400 did not return a -1 for weight"




    
    