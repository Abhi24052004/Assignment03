def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

num=input("Enter a number: ")
ans=factorial(int(num))
print(f"Factorial of {num } is: {ans}")