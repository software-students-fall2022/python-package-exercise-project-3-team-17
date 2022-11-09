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

def fat_problems(bmi):

    #validate number
    if not isinstance(bmi, float):
        raise Exception('Please make sure bmi is of type float')
        return
    
    if bmi < 10.0 or 50.0 < bmi:
        raise Exception('Please make sure bmi is in the range of 10.0 and 50.0 inclusive')
        return


    # data structures initialisation
    diseasesWithRiskLevel = {}
    diseases = []
    risk_levels = []

    # extreme underweight
    if bmi < 15.0:
        diseases = [11,12,13,16,19,20,21,22,23]
        risk_levels = [5,4,5,6,6,6,6,5,6]

    # underweight
    elif 15.0 <= bmi < 18.5:
        diseases = [11,12,13,16,19,20,21,22,23]
        risk_levels = [3,3,4,4,4,5,5,4,5]

    # normal weight
    elif 18.5 <= bmi < 25.0:
        diseases = [1,3,4,5,8,9,12,15,19,20,21,23]
        risk_levels = [1,2,1,2,1,1,1,1,1,1,2,2]
    
    # overweight
    elif 25.0 <= bmi < 30.0:
        diseases = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,21,23]
        risk_levels = [3,3,3,2,2,3,2,2,3,2,3,2,2,2,3,3,3,4,2,2]

    # obesity
    elif 35.0 <= bmi < 40.0:
        diseases = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,21,23]
        risk_levels = [4,5,3,3,5,4,3,5,4,4,5,4,4,3,4,4,4,5,4,3]
    
    # extreme obesity
    else:
        diseases = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,21,23]
        risk_levels = [6,5,6,6,5,4,5,5,4,6,5,6,4,6,5,4,4,6,4,3]

    for i in range(len(diseases)):
            diseasesWithRiskLevel[diseases_list[diseases[i]]] = levels_list[risk_levels[i]] 

    return diseasesWithRiskLevel
