def get_cities_name(city, country, population=''):
    """返回格式的城市,国家"""
    full_name = city + ',' + country + '-population ' + str(population)
    return full_name