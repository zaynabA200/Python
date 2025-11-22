# profit or loss

cp=int(input("enter the cost price :"))
sp=int(input("enter the selling price :"))
if cp < sp:
    print(f"{sp-cp} is the profit")
else:
    print(f"{cp-sp} is the loss amount")
