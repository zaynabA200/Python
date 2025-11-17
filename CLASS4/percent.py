#percentage calculation

maths=int(input("enter the maths marks:"))
science=int(input("enter the science marks:"))
english=int(input("enter english marks:"))
kashmiri=int(input("enter the kashmiri marks:"))

total=maths+science+english+kashmiri

per=total/400*100

print("The total marks are:",total)
print("The percentage is:",per)