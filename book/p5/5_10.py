current_users = ['admin', 'java', 'nginx', 'mysql', 'Nginx']
new_users = ['Admin', 'nginx', 'tomcat', 'apache', 'IIS']
for user in new_users:
    if user.lower() in current_users:
        print(user+"，please input other username")
    else:
        print(user+ ",this user not be userd")