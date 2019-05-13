with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents.strip())

print("\n")
file_name = 'learning_python.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line.strip())

print("\n")
file_name = 'learning_python.txt'
"""打印文件每行内容存储在列表中"""
pages = []
with open(file_name) as file_object:
    for line in file_object:
        pages.append(line)

for page in pages:
    message = "文本的内容是:" + page
    print(message.rstrip())
