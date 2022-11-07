# https://healthyeater.com/how-to-calculate-your-macros
def calculateREE(age, gender, height, weight, scale):
    '''
    calculates Resting Energy Expenditure (REE) using Mifflin-St Jeor formula
    '''
    if scale == 'i':
        #converting lbs to kgs and ft to cm
        weight = weight / 2.205
        height = height / 2.254
    elif scale != 'm':
        raise Exception("Invalid scale parameter. Please enter either \
            'i' for imperial or 'm' for metric")
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
def weightLossOrGainCalculator(TDEE, lossOrGain):
    '''
    calculates daily calorie consumption needed to lose or gain based on a user's TDEE

    lossOrGain parameter is either 'l' or 'g' and indicates whether the user \
    intends to lose or gain weight(i.e., build muscle)
    '''
    if lossOrGain != 'l' and lossOrGain != 'g':
        raise Exception("Invalid Loss or Gain parameter. Please enter either \
        'l' for loss or 'g' for gain")
    targetTDEE = TDEE - .2*TDEE if lossOrGain == 'l' else TDEE + .2*TDEE
    return targetTDEE

def macros(weight, targetTDEE, scale):

    if scale == 'm':
        weight = weight * 2.205
    elif scale != 'i':
        raise Exception("Invalid scale parameter. Please enter either \
            'i' for imperial or 'm' for metric")
    '''
    calculate ideal macronutrient ratios for a given weight and TDEE
    '''
    dailyProteinInGrams = .825 * weight
    dailyProteinInCalories = dailyProteinInGrams * 4

    dailyFatInCalories = .25 * targetTDEE
    dailyFatInGrams = dailyFatInCalories / 9

    dailyCarbsInCalories = targetTDEE - dailyFatInCalories - dailyProteinInCalories
    dailyCarbsInGrams = dailyCarbsInCalories / 4

    # return macro proportions in grams 
    macroDict = {
        'Protein Intake': dailyProteinInGrams,
        'Fat Intake': dailyFatInGrams,
        'Carb Intake': dailyCarbsInGrams
    }

    return macroDict
