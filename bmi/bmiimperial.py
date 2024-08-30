# For example, an execution could look like this:

#    Please enter weight in kilograms: 50
#    Please enter height in meters: 1.58
#    BMI is: 20.0288415318

weight = float(input("Please enter weight in pounds: "))
height = float(input("Please enter height in inches: "))
print(f"BMI is: {weight * 0.453592 / ((height * 0.0254) ** 2)}")
