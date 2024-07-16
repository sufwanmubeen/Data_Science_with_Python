#BMI calculator
print("This is BMI calculator:")
name = input("Enter your name: ")
weight = input("Enter your weight in kg:")
weight = int(weight)
height = input("Enter your height in meters: ")
height = int(height)
#BMI calculation formula
BMI = weight / (height * height)
print(name,"! Your BMI is", BMI)