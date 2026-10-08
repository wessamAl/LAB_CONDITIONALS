height = int(input("Enter your height in cm: "))
weight = int(input("Enter your weight in kg: "))

bmi = weight / ((height / 100) ** 2)

if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You have a normal weight.")
elif bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")


print("Your BMI is:", round(bmi, 2))