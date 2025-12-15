a = int(input("enter first number: "))
b= int(input("enter second number: "))

a, b = b, a
print("after swapping: ")
print("first number: ", a)
print("second number: ", b)