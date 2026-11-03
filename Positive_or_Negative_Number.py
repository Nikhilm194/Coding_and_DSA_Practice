#Brute-Force method
num = int(input("Enter the number"))
if(num >= 0):
    print("Number is positive")
else:
    print("Number is negative")

#Using Nested If-Else
num = int(input("Enter the number : "))
if(num>=0):
    if(num == 0):
        print("Number is zero")
    else:
        print("Number is positive")
else:
    print("Number is negative")  
     
# Using Ternary operator
num = int(input("Enter the number : "))
print("Positive" if num >= 0 else "Negative") 