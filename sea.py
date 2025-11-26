from water import Water

class Sea(Water):
    """Класс для морей"""
    def __init__(self, name, depth, salinity):
        super().__init__(name)
        self.depth = depth
        self.salinity = salinity
    
    @classmethod
    def create_from_input(cls, validator):
        """Создает море из пользовательского ввода"""
        print("\n--- Добавление нового моря ---")
        name = validator.safe_input("Введите название моря: ", "Название моря")
        depth = validator.safe_input("Введите глубину (м): ", "Глубина", 'float')
        salinity = validator.safe_input("Введите соленость (‰): ", "Соленость", 'float')
        
        return cls(name, depth, salinity)
    
    def to_file_format(self):
        """Возвращает строку для сохранения в файл"""
        return f'море "{self.name}" {self.depth} {self.salinity}'