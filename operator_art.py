#solution of 1
a = 10
b = 3

print(f"{'Addition':15}{'a + b':}{a + b:10}")
print(f"{'Subtraction':<15}{'a - b':<15}{a - b:<10}")
print(f"{'Multiplication':<15}{'a * b':<15}{a * b:<10}")
print(f"{'Division':<15}{'a / b':<15}{a / b:<10.2f}")
print(f"{'Modulus':<15}{'a % b':<15}{a % b:<10}")

#solution of 2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(f"{a} is greater than {b}")

elif a < b:
    print(f"{a} is less than {b}")

else:
    print(f"{a} is equal to {b}")

#solution of 3
num = int(input("Enter a number to check between 10 and 15: "))

if num >= 10 and num <= 15:
    print(f"{num} is between 10 and 15")
else:
    print(f"{num} is NOT between 10 and 15")

#solution of 4
num = int(input("Enter a number to check divisable by 3 and 5: "))

if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5")
else:
    print(f"{num} is NOT divisible by both 3 and 5")

