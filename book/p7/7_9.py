sandwich_orders = ['caomei', 'pastrami','orange', 'banana', 'pastrami', 'nimeng', 'pastrami']
print("Sorry,pastrami is 卖完了!!!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("curent_sandwich is following:")
for sandwich_order in sandwich_orders:
    print(sandwich_order)