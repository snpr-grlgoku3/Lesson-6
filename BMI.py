Height= float(input("Please enter your height in metres:"))
Weight= float(input("Please enter ypur weight in kilograms:"))
BMI= Weight/(Height**2)
if BMI <18.5:
    print("You are underweight")
elif BMI <24.9:
    print ("You are healthy")
elif BMI <29.9:
    print("You are overweight")
elif BMI <34.9:
    print("You are extremely overweight")
elif BMI<39.9:
    print("You are obese")
else:
    print("You are severly obese")