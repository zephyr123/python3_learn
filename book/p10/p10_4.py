filename = 'guest_book.txt'
while True:
    name = input("please input your name:")
    mes = name + ", Hello,welcom to here!"
    print(mes)
    with open(filename,'w') as file_object:
        file_object.write(name + "\n")
        file_object.write(mes + "\n")
    break

