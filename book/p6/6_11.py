cities = {
    'beijing': {
        'country': 'china',
        'populatin': '2000blions',
        'fact': '1500 years histroy'
    },
    'boston': {
        'country': 'Ameria',
        'populatin': '1000blions',
        'fact': '700 years histroy'
    }
}
for key,values in cities.items():
    print(key + ":")
    print("国家:" + values['country'])
    print("人口:" + values['populatin'])
    print("描述历史:" + values['fact'])