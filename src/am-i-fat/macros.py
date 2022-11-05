def calculateREE(age, gender, height, weight):
    '''
    calculates Resting Energy Expenditure (REE) using Mifflin-St Jeor formula
    '''
    # male version
    if gender == 'm':
        return 10 * weight + 6.25 * height - 5 * age + 5
    # female version
    elif gender == 'f':
        return 10 * 6.25 * height - 5 * age - 161
    else:
        raise Exception("invalid gender parameter. Input \
            'm' for male and 'f' for female.")

def calculateTDEE(REE, userActivityLevel):
    '''
    calculates Total Daily Energy Expenditure (TDEE) in 
    calories for a given REE and self-reported activity level
    from sedentary (1) to very active (4).
    
    - Consuming more than your TDEE = weight gain
    - Consuming less than your TDEE = weight loss
    - Consuming the same as your TDEE = weight maintenance
    '''
    activityLevelDict = {
        1: REE * 1.2,
        2: REE * 1.375,
        3: REE * 1.55,
        4: REE * 1.725
    }
    try:
        return activityLevelDict[userActivityLevel]
    except KeyError:
        raise Exception("Invalid Activity Level parameter. \
            Please enter a number from 1 (sedentary) to 4 (very active))")

def macros(age, gender, height, weight, activityLevel, goal, scale):

    return
