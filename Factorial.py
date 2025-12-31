#Factorial of a Number (While Loop)
num = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1

print("Factorial of", num, "is", factorial)
