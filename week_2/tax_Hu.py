income = int(input("Please enter your income:"))
if income<=1000:
    tax=income*0.05
elif income<=2000:
    tax=1000*0.05+(income-1000)*0.1
else:
    tax=1000*0.05+1000*0.1+(income-2000)*0.15
print("The tax you owned is: ",tax)