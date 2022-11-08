# Python Package Exercise

A little exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

[![Build & test](https://github.com/software-students-fall2022/python-package-exercise-project-3-team-17/actions/workflows/build.yaml/badge.svg?)](https://github.com/software-students-fall2022/python-package-exercise-project-3-team-17/actions/workflows/build.yaml)


## Description

This is a lightweight, health-focused package that offers the following functionality: <br>

<ol>
    <li>Calculates a user’s Body Mass Index determines where the user falls within the BMI scale, ranging from underweight to obese</li>
    <li>Identifies diseases associated with a certain, abnormal BMI level (underweight or overweight)</li>
    <li>Describes a balanced diet consisting of the amount, in grams, of proteins, carbohydrates, fat, sugar, saturated fats, as well as food energy in calories</li>
    <li>Calculates a user’s Active Metabolic Rate, with an option for the user to get his/her Basal Metabolic Rate.</li>
</ol>

## Features

<details>
<summary>Calculate a user's BMI and render obesity scale:</summary>

    howfat(age, height, weight, scale):
    //Returns bmi score, scale

    /More details about parameters:

    * age- integer value representing age
    * height- integer value representing height
        * metric - integer value in (cm)
        * imperial - integer value in (in)
    * weight- integer value representing weight
        * metric - integer value in (kg)
        * imperial - integer value in (lb)
    * scale
        "i" for imperial
        "m" for metric
    
    /Disclosure:
    BMI and its respective obesity scale may not reflect a precise overview of one's health conditions, especially for ages under 18 and above 65.
    
</details>

<details>
<summary>Return list of related diseases by BMI:</summary>

    fat_problems(bmi):
    //Returns related diseases

</details>

<details>
<summary>Calculate a user's recommended daily calorie intake: </summary>

    calories(age, gender, height, weight, activityLevel, scale):
    //Returns recommended daily calorie intake

    /More details about parameters

    * age- numeric value (integer) representing age
    * gender
        "f" for female
        "m" for male
    * height- numeric value representing height
    * weight- numeric value representing weight
    * activityLevel- numeric value (integer) representing a user's activity level
        Use scale below:
        0-Basal Metabolic Rate
        1-Sedentary: little or no exercise
        2-Lightly active: exercise 1-3 times a week
        3-Moderately active: exercise 3-5 times a week
        4-Active: exercise 6-7 times a week
        5-Very active: hard exercise 6-7 times a week
    * scale
        "i" for imperial
        "m" for metric


    


</details>

<details>

<summary>Calculate a user's resting energy expenditure</summary>

    calculateREE(age, gender, height, weight, scale):
    
    More details about parameters:

    * age - numeric value (integer) representing age
    * gender
        "f" for female
        "m" for male
    * height - numeric value representing height
    * weight - numeric value representing weight
    * scale
        "i" for imperial
        "m" for metric
    
</details>

<details>

<summary>Calculate a user's total daily energy expenditure</summary>

    calculateTDEE(REE, userActivityLevel)
    
    More details about parameters

    * REE - Resting Energy Expenditure in calories (how many calories burned at rest)

    * userActivityLevel- numeric value (integer) representing a user's activity level
        Use scale below:
        1 - Sedentary: Just everyday activities like a bit of walking, a couple of flights of stairs, eating, talking, etc. (REE X 1.2)

        2 - Lightly active: Any activity that burns an additional 200-400 calories for females or 250-500 calories for males. (REE x 1.375)

        3 - Moderately active: Any activity that burns an additional 400-650 calories for females or 500-800 calories for males. (REE x 1.55)
        
        4 - Very Active: Any activity that burns an additional 650+ calories for females or 800+ calories for males. (REE x 1.725)
    
</details>

<details>

<summary>Calculate a user's target TDEE for weight loss or gain</summary>

    weightLossOrGainCalculator(TDEE, lossOrGain)
    
    More details about parameters

    * weight - numeric value representing weight

    * lossOrGain
        'l' for loss - aiming to lose weight
        'g' for gain - aiming to gain weight
    * scale

    
</details>

<details>

<summary>Calculate ideal macronutrient ratios for a given weight and TDEE</summary>

    macros(weight, targetTDEE, scale)
    
    More details about parameters

    * TDEE - total daily energy expenditure in calories (amount of energy your body burns in a day)

    * lossOrGain
        'l' for loss - aiming to lose weight
        'g' for gain - aiming to gain weight
    
</details>

## How to Install and Use this Package

1. Navigate to your desired root directory and execute 

```
pipenv install -i https://test.pypi.org/simple/ amIFat==1.0.5
```

(Prof B's note: if you've previously created a pipenv virtual environment in the same directory, you may have to delete the old one first. Find out where it is located with the pipenv --venv command.)

2. Activate virtual environment with 
```
pipenv shell
```
3. Create a python program in the directory and import all the functions in the ```amIFat``` package with 

```
from amIFat import macros, howfat, calories, fat_problems
```
4. Implement the functions in your program and run it with 

```
python3 yourProgram.py
```
5. Exit the virtual environment with ```exit```

