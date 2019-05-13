num0 = input("please input first number:")
num1 = input("please input second number:")
try:
    num0 = int(num0)
    num1 = int(num1)
except:
    print("make true your input is a number!")
else:
    print(num0 + num1)