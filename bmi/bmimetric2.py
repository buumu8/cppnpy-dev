# For example, an execution could look like this:

#    Please enter weight in kilograms: 50
#    Please enter height in meters: 1.58
#    BMI is: 20.0288415318

weight = float(input("Please enter weight in kilograms: "))
height = float(input("Please enter height in meters: "))

bmi = weight / height / height

status = "Underweight"

if bmi >= 30.0:
    status = "Obese"
elif bmi >= 25.0:
    status = "Overweight"
elif bmi >= 18.5:
    status = "Normal"

print(f"BMI is: {round(bmi,2)}, Status is {status}")
