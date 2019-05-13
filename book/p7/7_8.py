sandwich_orders = ['caomei','orange','banana']
finished_sandwiches = []
while sandwich_orders:
    curent_sandwich = sandwich_orders.pop()
    print("I make your sandwich:" + curent_sandwich)
    finished_sandwiches.append(curent_sandwich)
print("\nThe following sandwiches is :")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())