pizzas = ['yidali', 'ameria', 'england']
friend_pizzas = pizzas[:]
pizzas.append('china')
friend_pizzas.append('yindu')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)