name=input("Enter your name: ")
count=len(name)
a=""
while count>=1:
    if count==len(name):
        a=a+name.upper()[count-1]
        print(name.upper()[count-1],end="")
        count -=1
    else:
        a=a+name.lower()[count-1]
        print(name.lower()[count-1],end="")
        count -=1
print("")
if name==a:
    print("Palindrome!")