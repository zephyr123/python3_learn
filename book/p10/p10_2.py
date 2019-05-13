file_name = 'learning_python.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line.replace('Python','C').strip())



