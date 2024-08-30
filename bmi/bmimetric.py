# For example, an execution could look like this:

#    Please enter weight in kilograms: 50
#    Please enter height in meters: 1.58
#    BMI is: 20.0288415318

weight = float(input("Please enter weight in kilograms: "))
height = float(input("Please enter height in meters: "))
print(f"BMI is: {weight / height / height}")
