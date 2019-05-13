import json
filename = 'number.json'
try:
    with open(filename) as f_obj:
        duqu = json.load(f_obj)

except FileNotFoundError:
    temp = input("Please input your like numbers:")
    with open(filename, 'w') as f_obj:
        json.dump(temp, f_obj)
else:
    print("I know your favorite number! It's " + duqu)
