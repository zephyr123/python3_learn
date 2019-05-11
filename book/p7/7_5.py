active = True
while active:
    age = input("Please input your age:")
    print(age)
    if age == 'quit':
        active = False
    elif int(age) < 3:
        print("This body is free!")
    elif int(age) < 12:
        print("This children is 10 dollar!")
    elif int(age) >= 12:
        print("price is 15 dollar!")

