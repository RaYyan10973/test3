import unittest
from unittest.mock import patch
from data_validator import DataValidator
from data_parser import DataParser
from lake import Lake
from sea import Sea
from river import River
from reservoir import Reservoir


class TestObjectCreation(unittest.TestCase):
    """Тесты создания объектов водных ресурсов"""
    
    def test_lake_creation_with_valid_data(self):
        """Тест создания объекта Lake с корректными данными"""
        lake = Lake("Байкал", 1642.0, 636.0)
        
        self.assertEqual(lake.name, "Байкал")
        self.assertEqual(lake.depth, 1642.0)
        self.assertEqual(lake.width, 636.0)
        self.assertIsInstance(lake, Lake)
    
    def test_sea_creation_with_valid_data(self):
        """Тест создания объекта Sea с корректными данными"""
        sea = Sea("Черное море", 2210.0, 18.0)
        
        self.assertEqual(sea.name, "Черное море")
        self.assertEqual(sea.depth, 2210.0)
        self.assertEqual(sea.salinity, 18.0)
        self.assertIsInstance(sea, Sea)
    
    def test_river_creation_with_valid_data(self):
        """Тест создания объекта River с корректными данными"""
        river = River("Волга", 254.0, 48.0, "1937", 3530.0)
        
        self.assertEqual(river.name, "Волга")
        self.assertEqual(river.volume, 254.0)
        self.assertEqual(river.fill_time, 48.0)
        self.assertEqual(river.creation_year, "1937")
        self.assertEqual(river.length, 3530.0)
        self.assertIsInstance(river, River)
    
    def test_reservoir_creation_with_valid_data(self):
        """Тест создания объекта Reservoir с корректными данными"""
        reservoir = Reservoir("Рыбинское", 112.0, "2980")
        
        self.assertEqual(reservoir.name, "Рыбинское")
        self.assertEqual(reservoir.length, 112.0)
        self.assertEqual(reservoir.water_flow, "2980")
        self.assertIsInstance(reservoir, Reservoir)


class TestDataParser(unittest.TestCase):
    """Тесты парсера данных"""
    
    def setUp(self):
        self.parser = DataParser()
    
    def test_parse_reservoir_line_success(self):
        """Тест успешного парсинга строки с водохранилищем"""
        test_line = 'водохранилище "Рыбинское" 112 2980'
        
        result = self.parser.parse_line(test_line)
        
        self.assertEqual(result['object_type'], 'водохранилище')
        self.assertEqual(result['name'], 'Рыбинское')
        self.assertEqual(result['numbers'], ['112', '2980'])


def run_creation_tests():
    """Запуск всех тестов создания объектов"""
    print(" ТЕСТИРОВАНИЕ СИСТЕМЫ ВОДНЫХ ОБЪЕКТОВ")
    print("=" * 50)
    
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Добавляем только указанные тестовые классы
    suite.addTests(loader.loadTestsFromTestCase(TestObjectCreation))
    suite.addTests(loader.loadTestsFromTestCase(TestDataParser))
    
    # Запускаем тесты
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Выводим итоги
    print("=" * 50)
    print(" РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ:")
    print(f"   Всего тестов: {result.testsRun}")
    print(f"   Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"   Провалов: {len(result.failures)}")
    print(f"   Ошибок: {len(result.errors)}")
    
    if result.wasSuccessful():
        print(" ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
    else:
        print(" ОБНАРУЖЕНЫ ПРОБЛЕМЫ!")
    
    return result.wasSuccessful()


if __name__ == '__main__':
    run_creation_tests()