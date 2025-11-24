#bmi checker    
w=float(input("enter the weight in kgs:"))
h=float(input("enter the height in meters"))

bmi=w/(h**2)
print("the bmi is",round(bmi,2))
if bmi<18.5:
    print("you are underweight")
elif bmi < 25:
    print("you are healthy")
elif bmi< 30:
        print("you are overweight")
else:
        print("you are obese")
