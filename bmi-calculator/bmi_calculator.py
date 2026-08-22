# First get the inputs from the user
name = input("What's your name: ")
weight =  int(input("Enter your weight in pounds: "))
height = int(input("Enter your height in inches: "))

# Calculating and Displaying the results
BMI = round((weight * 703) / (height*height), 2)
print(BMI)

# Let's put some conditions to categorize based on the BMI
if BMI>0:
    if BMI<18.5:
        print(name+ " your BMI is " + str(BMI) + " and you are underweight.")
    elif BMI<24.9:
        print(name+ " your BMI is " + str(BMI) + " and you are normal weight.")
    elif BMI<29.9:
        print(name+ " your BMI is " + str(BMI) + " and you are overweight.")
    elif BMI<34.9:
        print(name+ " your BMI is " + str(BMI) + " and you are obese.")
    elif BMI<39.9:
        print(name+ " your BMI is " + str(BMI) + " and you are severely obese.")
    else:
        print(name+ " your BMI is " + str(BMI) + " and you are morbidly obese.")
else:
    print("Please, enter accurate inputs.")
