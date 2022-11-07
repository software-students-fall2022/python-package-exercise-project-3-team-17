import pytest
import random 
from calories import*
class Tests:

  

#------------------------------------calories() UNIT TESTS-----------------------------------
#--------------Valid input test for calories()-----------------
    ''' Valid input criteria:
        (1) Make sure calories() returns a valid caloric measurement 
        (2) Make sure calories() returns a number
        (3) Make sure calories() returns a positive integer
        '''
#Make sure calories() returns a valid caloric measurement 
def test_calories_with_valid_inputs():
    #Hand written calculations based off of verywellfit.com
    #age=22,gender="f", height=63,weight=120,activityLevel=3,scale="i"
    actual=calories(22,"f",63,120,2,"i")
    assert actual==1883, "calories() did not return the expected calories"


#Make sure calories() returns a positive integer
def test_calories_with_valid_inputs_return_positive_number():
    for i in range(10):
        #Test with scale=metric
        actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),random.randint(1,5),"m")
        assert type(actual)==int,"calories() did not return an integer under the metric scale"
        assert actual>0, "calories() did not return an positive value under the metric scale"

        #Test with scale=imperial
        actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(55,80),random.randint(80,400),random.randint(1,5),"i")
        
        assert type(actual)==int,"calories() did not return an integer under the imperial scale"
        assert actual>0, "calories() did not return an positive value under the imperial scale"
        
        

"""Criteria regarding invalid input for calories():
    *Note: "not accepted" means that calories() returns a value of -1
    (1) Make sure an age that falls out of the range of 1 and 120 is not accepted
    (2) Make sure gender other than "f" and "m" are not accepted
    (3) Make sure for height and weight, values other than numbers are not accepted 
    (4) Make sure height outside the range 1 and 107 and for weight 1 and 1400 
            are not accepted (imperial)
    (5) Make sure height outside the range 1 and 272 and for weight 1 and 635 
            are not accepted (metric)
    (6) Make sure scale other than "i" and "m" are not accepted
    (7) Make sure entries for activity levels that are not whole numbers and not within the range
            of 0 and 5 are not accepted
"""
#--------------Invalid input tests for calories()-----------------
#Make sure an age that falls out of the range of 1 and 120 is not accepted 
def test_calories_with_invalid_inputs_age():
    #Test with scale=metric 
    actual=calories(-1,random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),random.randint(1,5),"m")
    assert actual==-1,"Age less than 1 did not return -1"
    actual=calories(500,random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),random.randint(1,5),"m")
    assert actual==-1,"Age greater than 120 did not return -1"

#Make sure gender other than "f" and "m" are not accepted
def test_calories_with_invalid_inputs_gender():
    #Test with scale=metric 
    #Put "female" instead of f
    actual=calories(random.randint(18,100),"female",
        random.randint(150,195),random.randint(45,100),random.randint(1,5),"m")
    assert actual==-1, "An invalid value for gender did not return -1"

#Make sure for height and weight, values other than numbers are not accepted
def test_calories_with_invalid_inputs_height_and_weight_type():
    #Test with scale=metric 
    #Put a string in for height
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        "height",random.randint(45,100),random.randint(1,5),"m")
    assert actual==-1,"A non numeric value for height did not return -1"

    #Put a string in for weight
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),"weight",random.randint(1,5),"m")
    assert actual==-1, "A non numeric value for weight did not return -1"

#Make sure height outside the range 1 and 107 and for weight 1 and 1400 are not accepted (imperial)
def test_calories_with_invalid_inputs_height_and_weight_ranges_imperial():
    #Test with scale=metric 
    #height below 1
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        -100,random.randint(80,350),random.randint(1,5),"i")
    assert actual==-1,"A value less than 1 for height did not return -1 (imperial)"
    #weight below 1
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(55,75),-100,random.randint(1,5),"i")
    assert actual==-1, "A value less than 1 for weight did not return -1 (imperial)"
    #height above 107
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        200,random.randint(80,350),random.randint(1,5),"i")
    assert actual==-1,"A value above 107 for height did not return -1 (imperial)"
    #weight above 1400
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(55,75),7000,random.randint(1,5),"i")
    assert actual==-1, "A value above 1400 for weight did not return -1 (imperial)"

#Make sure height outside the range 1 and 272 and for weight 1 and 635 are not accepted (metric)
def test_calories_with_invalid_inputs_height_and_weight_ranges_metric():
    #Test with scale=imperial 
    #height below 1
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        -100,random.randint(45,100),random.randint(1,5),"m")
    assert actual==-1,"A value less than 1 for height did not return -1 (metric)"
    #weight below 1
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),-100,random.randint(1,5),"m")
    assert actual==-1, "A value less than 1 for weight did not return -1 (metric)"
    #height above 272
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        500,random.randint(45,100),random.randint(1,5),"m")
    assert actual==-1,"A value above 107 for height did not return -1 (metric)"
    #weight above 635
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),1000,random.randint(1,5),"m")
    assert actual==-1, "A value above 1400 for weight did not return -1 (metric)"

#Make sure scale other than "i" and "m" are not accepted
def test_calories_with_invalid_inputs_scale():
        #Test with scale=metric 
        #Put "metric" instead of "m"
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),random.randint(1,5),"metric")
    assert actual==-1,"An invalid value for scale did not return -1"

#Make sure entries for activity levels that are not whole numbers and not within the range
#of 0 and 5 are not accepted
def test_calories_with_invalid_inputs_activityLevel():
    #Test with scale=metric
    #activityLevel below 0
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),-1,"m")
    assert actual==-1, "A value below 1 for activityLevel did not return -1"

    #activityLevel above 5
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),10,"m")
    assert actual==-1, "A value above 5 for activityLevel did not return -1"

    #Test non-whole number
    actual=calories(random.randint(18,100),random.choice(["m","f"]),
        random.randint(150,195),random.randint(45,100),10.5,"m")
    assert actual==-1, "A non-whole number for activityLevel did not return -1"
    


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

    assert type(actual1)==float, "Did not return a numeric height"
    assert type(actual2)==float, "Did not return a numeric weight"

#Make sure return values are positive
def test_convertScale_return_positive():
    actual1, actual2=convertScale(random.randint(55,72),random.randint(80,350))
    assert actual1>0, "Did not return a positive height"
    assert actual2>0, "Did not return a positive weight"



'''
Invalid input criteria:
*Note: "not accepted" means that convertScale() returns a value of -1
(1) Make sure height out of range 1-107 are not accepted
(2) Make sure weight out of range of 1-1400 are not accepted
'''  

#--------------Invalid input tests for convertScale()-----------------

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




    
    