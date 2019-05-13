input("input 'q' to quit.")
while True:
    num0 = input("please input first number:")
    if num0 == 'q':
        break
    num1 = input("please input second number:")
    if num1 == 'q':
        break

    try:
        num0 = int(num0)
        num1 = int(num1)
    except:
        print("make true your input is a number!")
    else:
        print(num0 + num1)