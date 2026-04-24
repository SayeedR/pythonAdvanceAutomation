#solution of 1
a = "hello"
b = 25
c = 3.14
d = True

print(f"a = {a}, type = {type(a).__name__}")
print(f"a = {b}, type = {type(b).__name__}")
print(f"a = {c}, type = {type(c).__name__}")
print(f"a = {d}, type = {type(d).__name__}")

#solution of 2
a = input("Enter something so that i can help you to find it's datatype:")
print(f"Value {a}")
print(f"type {type(a).__name__}")

#solution of 3

a = input("Enter a value: ")

try:
    a = int(a)
    print(f"Value: {a}")

except ValueError:
    try:
        a = float(a)
        print(f"Value: {a}")
    except ValueError:
        print(f"Value: {a}")

