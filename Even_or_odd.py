# Brute Force method
num = int(input("Enter the number : "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Using Ternary operator
num = int(input("Enter the number : "))
print("Even" if num % 2 == 0 else "Odd")

# Using Bitwise operator
def isEven(num):
    return not num&1
if __name__ == "__main__":
    num = int(input("Enter the number : "))
    if isEven(num):
        print("Even")
    else:
        print("Odd")
