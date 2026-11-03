# First using the For Loop
num = int(input("Enter a number : "))
sum = 0
for i in range(1, num+1):
    sum = sum + i
print("The sum of first", num, "natural numbers is :", sum)

# Using the formula
num = int(input("Enter a number : "))
print(int(num * (num + 1) / 2))

# Using Recusion
def getsum(num):
    if num == 1:
        return 1
    else:
        return num + getsum(num - 1)
num = int(input("Enter a number : "))
print("The sum of first", num, "natural numbers is :", getsum(num))