#validate number
def valid_num(n):
    if isinstance(n,int):
        return True
    else:
        return False

#validate scale
def valid_scale(c):
    if (c=="i" or c=="m"):
        return True
    else: 
        return False

#BMI scale
def BMI_scale(o):
    if (o<18.5):
        return "You are underweight"
    elif (18.5<=o<25):
        return "You are healthy"
    elif (25 <=o<30):
        return "You are overweight"
    elif (30<=o):
        return "You are obese"
    
#staticmain
def howfat(age, height, weight, scale, error=0) :
    '''
    Returns the Body Mass Index (BMI) and its corresponding description on the weight scale.
    Arguments taken are age, height, weight and scale.
    - Valid integer values should be passed for age, height and weight or will return an error.
    - For both imperial and metric, all height measurements must be rounded to the nearest integer value (the deviation from rounding can be considered miniscule in calculating BMI)
    - For imperial scale, height argument must be passed in inches. (i.e. 5ft=60)
    - Scale argument must be defined by a single string: "m" (metric) or "i" (imperial).
    BMI calculation formula derived from:
    imperial: https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_2.html#:~:text=When%20using%20English%20measurements%2C%20ounces,a%20conversion%20factor%20of%20703.
    metric: https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_1.html
    BMI to Obesity Scale is from:
    https://www.cdc.gov/obesity/basics/adult-defining.html
    '''
    if (valid_num(age)==True and valid_num(height)==True and valid_num(weight)==True and valid_scale(scale)==True) :
        if (18<=age<=65):
            if (scale == "i"):
                BMI = round((weight/height/height)*703,2)
                obesity = BMI_scale(BMI)
                return BMI,obesity
            elif (scale == "m"):
                BMI = round((weight/height/height)*10000,2)
                obesity = BMI_scale(BMI)
                return BMI,obesity
        else:
            if (scale == "i"):
                error_msg = "Please note that BMI for children, teens and seniors may not be accurate."
                BMI = round((weight/height/height)*703,2)
                obesity = BMI_scale(BMI)
                return error_msg,BMI,obesity
            elif (scale == "m"):
                error_msg = "Please note that BMI for children, teens and seniors may not be accurate."
                BMI = round((weight/height/height)*10000,2)
                obesity = BMI_scale(BMI)
                return error_msg,BMI,obesity
    else:
        raise Exception('Please check age, height, weight are integer values and scale is "i" or "m"')

