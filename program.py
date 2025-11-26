from data_parser import DataParser
from data_validator import DataValidator
from lake import Lake
from sea import Sea
from river import River
from reservoir import Reservoir


class Program:
    """Главный класс программы"""
    
    def __init__(self):
        self.parser = DataParser()
        self.validator = DataValidator()
        self.objects = []  # Единый список всех объектов
        self.data_file = "water_data.txt"
    
    def create_object_from_parsed_data(self, parsed_data):
        """Создает объект из распарсенных данных"""
        object_type = parsed_data['object_type']
        name = parsed_data['name']
        numbers = parsed_data['numbers']
        
        if object_type == 'озеро':
            if len(numbers) < 2:
                raise ValueError("Для озера нужно 2 числа: глубина и ширина")
            depth = self.validator.validate_float(numbers[0], "Глубина озера")
            width = self.validator.validate_float(numbers[1], "Ширина озера")
            return Lake(name, depth, width)
        
        elif object_type == 'море':
            if len(numbers) < 2:
                raise ValueError("Для моря нужно 2 числа: глубина и соленость")
            depth = self.validator.validate_float(numbers[0], "Глубина моря")
            salinity = self.validator.validate_float(numbers[1], "Соленость моря")
            return Sea(name, depth, salinity)
        
        elif object_type == 'река':
            if len(numbers) < 4:
                raise ValueError("Для реки нужно 4 параметра: объем, время наполнения, год создания, длина")
            volume = self.validator.validate_float(numbers[0], "Объем реки")
            fill_time = self.validator.validate_float(numbers[1], "Время наполнения реки")
            creation_year = self.validator.validate_date(numbers[2], "Год создания реки")
            length = self.validator.validate_float(numbers[3], "Длина реки")
            return River(name, volume, fill_time, creation_year, length)
        
        elif object_type == 'водохранилище':
            if len(numbers) < 2:
                raise ValueError("Для водохранилища нужно 2 параметра: длина и расход воды")
            length = self.validator.validate_float(numbers[0], "Длина водохранилища")
            water_flow = numbers[1]  # расход воды может быть строкой
            return Reservoir(name, length, water_flow)
        
        else:
            raise ValueError(f"Неизвестный тип объекта: {object_type}")
    
    def process_line(self, line):
        """Обрабатывает одну строку из файла"""
        try:
            # Парсим строку в словарь
            parsed_data = self.parser.parse_line(line)
            
            # Создаем объект из словаря
            water_object = self.create_object_from_parsed_data(parsed_data)
            
            # Добавляем в список
            self.objects.append(water_object)
            
            return water_object
            
        except Exception as e:
            print(f"Ошибка обработки строки: {e}")
            return None
    
    def load_from_file(self, filename=None):
        """Загружает данные из файла"""
        if filename is None:
            filename = self.data_file
        
        print(f"Загрузка данных из файла: {filename}")
        
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            
            successful = 0
            failed = 0
            
            for line_num, line in enumerate(lines, 1):
                line = line.strip()
                if not line:  # Пропускаем пустые строки
                    continue
                    
                print(f"🔍 Обработка строки {line_num}: {line}")
                result = self.process_line(line)
                
                if result:
                    successful += 1
                    print(f"Успешно: создан {type(result).__name__} '{result.name}'")
                else:
                    failed += 1
                    print(f"Ошибка в строке {line_num}")
            
            print(f"\n Итоги загрузки:")
            print(f"Успешно: {successful}")
            print(f"Ошибок: {failed}")
            print(f"Всего объектов: {len(self.objects)}")
            
        except FileNotFoundError:
            print(f"Файл {filename} не найден")
        except Exception as e:
            print(f"Ошибка чтения файла: {e}")
    
    def add_object_from_input(self, object_type):
        """Добавляет новый объект через пользовательский ввод"""
        try:
            if object_type == 'lake':
                obj = Lake.create_from_input(self.validator)
            elif object_type == 'sea':
                obj = Sea.create_from_input(self.validator)
            elif object_type == 'river':
                obj = River.create_from_input(self.validator)
            elif object_type == 'reservoir':
                obj = Reservoir.create_from_input(self.validator)
            else:
                print(" Неизвестный тип объекта")
                return None
            
            self.objects.append(obj)
            
            # Сохраняем в файл
            self.save_object_to_file(obj)
            
            print(f"{type(obj).__name__} '{obj.name}' успешно добавлен!")
            return obj
            
        except Exception as e:
            print(f" Ошибка добавления объекта: {e}")
            return None
    
    def save_object_to_file(self, water_object):
        """Сохраняет объект в файл"""
        try:
            with open(self.data_file, 'a', encoding='utf-8') as file:
                file.write(water_object.to_file_format() + '\n')
        except Exception as e:
            print(f" Ошибка сохранения в файл: {e}")
    
    def get_objects_by_type(self, object_type):
        """Возвращает объекты определенного типа"""
        type_map = {
            'lake': Lake,
            'sea': Sea,
            'river': River,
            'reservoir': Reservoir
        }
        
        if object_type not in type_map:
            return []
        
        return [obj for obj in self.objects if isinstance(obj, type_map[object_type])]
    
    def get_statistics(self):
        """Возвращает статистику по объектам"""
        stats = {
            'lakes': len(self.get_objects_by_type('lake')),
            'seas': len(self.get_objects_by_type('sea')),
            'rivers': len(self.get_objects_by_type('river')),
            'reservoirs': len(self.get_objects_by_type('reservoir')),
            'total': len(self.objects)
        }
        return stats