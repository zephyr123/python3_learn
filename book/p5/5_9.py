users = ['admin', 'sql', 'redis', 'www', 'nginx']
del users[:]
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin,would you like to see a status report")
        else:
            print("Hello "+user+",thank you for logging in again")
else:
    print("wo need to find some users")