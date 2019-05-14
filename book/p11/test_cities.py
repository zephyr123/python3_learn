import unittest
from city_functions import get_cities_name

class CitiesTestCase(unittest.TestCase):
    """测试city_functions.py方法"""
    def test_city_country(self):
        """测试国家和城市的方法"""
        full_name = get_cities_name('beijing', 'China')
        self.assertEqual(full_name,'beijing,China-population ')

    def test_city_country_population(self):
        full_name = get_cities_name('santiago', 'chile', population=5000000)
        self.assertEqual(full_name,'santiago,chile-population 5000000')
unittest.main()
