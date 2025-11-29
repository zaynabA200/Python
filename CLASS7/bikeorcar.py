# customize your ride

choice =input("1.Bike\n2.car\nEnter your choice:")
if choice =="1":
    choice2=input("1.Scooty\n2.Royal Enfeild\nEnter your choice:")
    if choice2=="1":
        print("you have selected scooty")
    elif choice2=="2":
            print("you have selected Royal Enfeild")
    else:
         print("Invalid Input")
elif choice=="2":
    choice2=input("1.Toyota\n2.Mercedes\nEnter your choice:")
    if choice2=="1":
            print("you have selected Toyota")
    elif choice2=="2":
            print("you have selected Mercedes")
    else:
         print("Invalid Input")
else:
      print("Invalid input")
  