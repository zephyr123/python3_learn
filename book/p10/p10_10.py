filename = 'test.txt'
with open(filename) as f_obj:
    contents = f_obj.read()
    num = contents.lower().count('the')
    print("this book has " + str(num)  + " 个 the letters.")
