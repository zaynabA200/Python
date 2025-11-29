#exam eligibility check

mc=input("Do you have a medical cause (y/n) :")

if mc.lower()=='n':
    att=int(input("enter the attendance :"))
    if att<75:
        print("you are not eligible to write the exam")
    else:
        print ("you are eligible:")
elif mc.lower()=='y':
    print("you are eligible")
else:
    print("invalid input")
