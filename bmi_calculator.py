hieght = float(input("Whats your hieght in inch?"))
weight = float(input("Whats your weight in pounds?"))
bmi = (weight*703)/(hieght*hieght)
print(str(round(bmi, 2)))
if bmi < 16.0:
    print("Severely Underweight ")
elif bmi > 16.0 and bmi < 18.4:
    print("Underweight")
elif bmi > 18.5 and bmi < 24.9:
    print("Normal") 
elif bmi > 25.0 and bmi < 29.9:
    print("Overweight") 
elif bmi > 30.0 and bmi < 34.9:
    print(" Moderately Obese") 
elif bmi > 35.0 and bmi < 39.9:
    print("Severely Obese")
elif bmi > 39.9:
    print(" Morbidly Obese")
else:   
    print('error')
