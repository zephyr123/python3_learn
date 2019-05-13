responses = {}
active = True
while active:
    name = input("what is your name:")
    place = input("where would you go:")
    responses[name] = place
    repeat = input("would you  like to another person respond? (yes or no)")
    if repeat == 'no':
        active = False
print("\n ---------调查结果如下--------")
for name,place in responses.items():
    print(name + " like to " + place + ".")