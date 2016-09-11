a=float(input("Enter a number: "))
b=float(input("Enter another number: "))
c=input("Enter a type of average (arithmetic,geometric or root-mean-square): ")
if c=='arithmetic':
    d=(a+b)/2
    print("The arithmetic average is: ",d)
elif c=='geometric':
    d=(a*b)**0.5
    print("The geometric mean is: ",d)
elif c=='root-mean-square':
    d=((a**2+b**2)/2)**0.5
    print("The root-mean-square is: ",d)
else:
    print("Please enter a valid type of average from the list.")