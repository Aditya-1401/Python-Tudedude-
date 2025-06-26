#Task 1 --> Calculate Factorial Using a Function

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

a = int(input("Enter the number = "))
print("Factorial of", a, "is", factorial(a))