from data_validator import DataValidator


class DataParser:
    """Класс для парсинга строк с данными"""
    
    def __init__(self):
        self.validator = DataValidator()
    
    def parse_line(self, line):
        """Парсит одну строку и возвращает словарь с данными"""
        line = line.strip()
        if not line:
            raise ValueError("Пустая строка")
        
        # Разбиваем строку на части
        parts = line.split('"')
        if len(parts) < 3:
            raise ValueError("Неправильный формат строки. Ожидается: тип \"название\" числа")
        
        object_type = parts[0].strip()
        name = parts[1].strip()
        numbers_str = parts[2].strip()
        numbers = numbers_str.split()
        
        # Возвращаем словарь с сырыми данными
        return {
            'object_type': object_type,
            'name': name,
            'numbers': numbers,
            'original_line': line
        }