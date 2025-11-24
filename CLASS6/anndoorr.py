#and or operator

a=10
b=-10
c=0
if a and b and c:
    print("all the variables have boolean value True")
else:
    print("atleast one of the variables have boolean value false")

    a=10
    b=-13
    c=11
    if a>0 or b>0:
        print("either of the values is greater than zero")
    else:
        print("None of the values is greater than zero")