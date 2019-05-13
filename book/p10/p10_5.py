filename = 'answer.txt'
input("please input 'q'  to exit")
while True:
    temp = input("please input your why you like coding:")
    if temp != 'q':
        with open(filename,'a') as file_object:
            file_object.write(temp + "\n")
    else:
        break