names = ['li yue', 'liu fang', 'pang leilei']
names[2] = 'zhang shengchao'
for name in names:
    message = name.title() + ",Welcome to my home!"
    print(message)
print("Pang Leilei,can't to my home!")
print("I find a big canting!")
names.insert(0,'chen xiaohua')
names.insert(2,'du xiaorui')
names.append('xiao pang')
for name in names:
    message = name.title() + ",Welcome to my home!"
    print(message)
print("Sorry,I just to yaoqing 2 ren！")
while len(names) > 2:
    pop_name = names.pop()
    print(pop_name.title() + ",Sorry,I can't yaoqing you!")
for name in names:
    message = name.title() + ",Welcome to my home!"
    print(message)
del names[:]
print(names)