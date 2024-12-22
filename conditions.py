
age = int(input("Enter your age: \n"))

if age >= 18:
    print("You are an adult.")
    print("You can drive.")
else:
    print("You are still a child")


temp_scale = input("Please enter the temperature scale (C/F/K): \n")

if temp_scale not in ['C', 'F', 'K']:
    print("Invalid temperature scale")
    exit()

temparature = float(input("Enter your temperature: \n"))

# convert temperature
if temp_scale == 'C':
    temp_f = (temparature * 9/5) + 32
    print(f"Temperature in Fahrenheit is {temp_f:.2f}")
elif temp_scale == 'F':
    temp_c = (temparature - 32) * 5/9
    print(f"Temperature in Celsius is {temp_c:.2f}")
elif temp_scale == 'K':
    temp_c = temparature - 273.15
    print(f"Temperature in Celsius is {temp_c:.2f}")
else:
    print("Invalid temperature scale")

exam_score = int(input("Enter your exam score: \n"))

if exam_score >= 90:
    grade = "A"
elif exam_score >= 80:
    grade = "B"
elif exam_score >= 70:
    grade = "C"
elif exam_score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}")
