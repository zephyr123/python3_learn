from collections import OrderedDict

computers = OrderedDict()

computers['OS'] = 'Linux'
computers['language'] = 'java'
computers['data'] = 'mysql'
computers['nosql'] = 'redis'

for key,value in computers.items():
    print("计算机对应的语言：" + key + ":" + " " + value)

