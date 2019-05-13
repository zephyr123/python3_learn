filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    try:
        with open(filename) as f_obj:
            print(f_obj.read())
    except FileNotFoundError:
        pass