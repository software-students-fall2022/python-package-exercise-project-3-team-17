import math

#--------------------------------convertScale()----------------------------
#Convert from imperial to metric
def convertScale(height,weight):
    #Invalid height and weight entries
    if type(height)!=float and type(height)!=int:
        return -1,-1
    if type(weight)!=float and type(weight)!=int:
        return -1,-1
    #height and weight boundaries
    if height<1 or height>107:
        return -1,-1
    if weight<1 or weight>1400:
        return -1,-1
    height=float(round(height*2.54,2))
    weight=float(round(weight*0.45359237,8))
    return height,weight


#------------------------------------calories()--------------------------------------
'''activityLevel 
    *0-Basal Metabolic Rate
    *1-Sedentary: little or no exercise
    *2-Lightly active: exercise 1-3 times a week
    *3-Moderately active: exercise 3-5 times a week
    *4-Active: exercise 6-7 times a week
    *5-Very active: hard exercise 6-7 times a week
'''
#Calculates the user's recommended daily calorie intake based on their AMR
def calories(age,gender,height,weight,activityLevel,scale):
    #^^^^^^^^^^INVALID INPUT CATCHES^^^^^^^^^^
    #Invalid age type
    if type(age)!=int:
        return -1
    #Invalid age
    if age<1 or age>120:
        return -1
    #Invalid gender entry
    if gender!="f" and gender!="m":
        return -1
    #Invalid height and weight entries
    if type(height)!=float and type(height)!=int:
        return -1
    if type(weight)!=float and type(weight)!=int:
        return -1
    #Invalid scale
    if scale!="i" and scale!="m":
        return -1
    #height and weight restrictions
    if scale=="i":
        if height<1 or height>107:
            return -1 
        if weight<1 or weight>1400:
            return -1
    if scale=="m":
        if height<1 or height>272:
            return -1 
        if weight<1 or weight>635:
            return -1 
    #Invalid activity level type
    if type(activityLevel)!=int:
        return -1
    #Invalid activity level range
    if activityLevel<0 or activityLevel>5:
        return -1
   
   
    
    #^^^^^^^^^^CALCULATIONS^^^^^^^^^^
    #******* Convert scale *******  
    if scale=="i":
        height,weight=convertScale(height,weight)

    #******* First calculate the user's BMR *******
    #Calculation for a female
    if gender=="f":
        bmr=655.1 + (9.563*weight) + (1.850*height)-(4.676*age)
    #Calculation for a male
    elif gender=="m":
        bmr=66.47+(13.75*weight)+(5.003*height)-(6.755*age)
       
    
    #******* Calculate by activity level *******
    if activityLevel==0:
        amr=bmr
    elif activityLevel==1:
        amr= bmr*1.2
    elif activityLevel==2:
        amr= bmr*1.375
    elif activityLevel==3:
        amr= bmr*1.55
    elif activityLevel==4:
        amr= bmr*1.725
    elif activityLevel==5:
        amr= bmr*1.9
    
    # return AMR
    return math.ceil(amr)


    

