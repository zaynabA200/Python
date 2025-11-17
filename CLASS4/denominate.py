#denomination calculator

amt=int(input("enter the amount: "))

note1=(amt//100)
note2=(amt%100//50)
note3=((amt%100)%50)//10
print("the count of 100 rupee notes are ",note1)
print("the count of 50 rupee notes are ",note2)
print("the count of 10 rupee notes are ",note3)