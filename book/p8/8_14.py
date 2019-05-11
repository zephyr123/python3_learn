def make_car(product,type,**car_info):
    car={}
    car['product']=product
    car['type']=type
    for key,value in car_info.items():
        car[key]=value
    return car

car=make_car('subaru','outback',color='blue',tow_package=True)
print(car)