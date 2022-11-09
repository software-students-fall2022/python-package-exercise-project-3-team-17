from amIFat.macros import *
from amIFat.calories import *
from amIFat.howfat import *
from amIFat.fat_problems import *

def main():
    #howfat
    print("Module: howfat")
    print('Testing howfat(age, height, weight, scale) with age=25, height=72, weigh=190, scale="i" ')
    print('Returning bmi score and obesity scale')
    print(howfat(25,72, 190, "i"))
    print("-------------------------------------------------------------------------------------------------------")

    #calories
    print("Module: calories")
    print('\nTesting calories(age, gender, height, weight, activityLevel, scale) with age=22, gender= "f", height=63, weigh=120, activityLevel=2, scale="i" ')
    print('Returning daily calorie intake (Active Metabolic Rate)')
    print(calories(22,"f",63,120,2,"i"))
    print("-------------------------------------------------------------------------------------------------------")
    
    #macros
    print("Module: macros")
    print("\nTesting calculateREE(age, gender, height, weight, scale) with age=21, gender='m', height=175, weight=80, scale='m' ")
    print('Returning resting energy expenditure ')
    ree=calculateREE(21, 'm', 175, 80, 'm')
    print(ree)
    
    print("\nTesting calculateTDEE(REE, userActivityLevel) with REE=" + str(ree) + ", userActivityLevel=4")
    print('Returning total daily energy expenditure')
    print(calculateTDEE(ree, 4))

    print("\nTesting weightLossOrGainCalculator(TDEE, lossOrGain) with TDEE=50, lossOrGain='g' ")
    print('Returning target TDEE for weight loss or gain')
    print(weightLossOrGainCalculator(50, 'g'))

    print("\nTesting macros(weight, targetTDEE, scale) with weight=36.2811791383, targetTDEE=3000000, scale='m'")
    print("Returning ideal macronutrient ratios for a given weight and TDEE")
    print(macros(36.2811791383, 3000000, 'm'))

    #fat_problems
    print("Module: fat_problems")
    print('\nTesting fat_problems(bmi) with bmi=32.0 ')
    print('Returning the diseases with risk levels')
    print(fat_problems(32.0))
    print("-------------------------------------------------------------------------------------------------------")    
   
main()
