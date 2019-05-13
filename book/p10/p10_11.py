import json
temp = input("Please input your like numbers:")

filename = 'number.json'
with open(filename,'w') as f_obj:
    json.dump(temp, f_obj)

with open(filename) as f_obj:
    duqu = json.load(f_obj)
    print("I know your favorite number! It's " + duqu)