# Question 16(b)
# Examination Number: Alessando Bellassai

# read weight

def display_intro():
    print('welcome to my BMI calculator!')
    weight = int(input("Enter weight (in kilograms): "))
    height = int(input("Enter height (in centimetres): ")) # centimetres
    bmi = weight / (pow(height,2)) * 10000
    print('BMI is: ', round(bmi, 1))
    
    if bmi < 18.5:
        print('Underweight')
    elif 18.5 < bmi < 24.9:
        print('Normal')
    elif 25 < bmi < 29.9:
        print('Overweight')
    elif bmi > 30:
        print('Obese')
        
display_intro()
