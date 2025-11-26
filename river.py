from water import Water

class River(Water):
    """Класс для рек"""
    def __init__(self, name, volume, fill_time, creation_year, length):
        super().__init__(name)
        self.volume = volume
        self.fill_time = fill_time
        self.creation_year = creation_year
        self.length = length
    
    @classmethod
    def create_from_input(cls, validator):
        """Создает реку из пользовательского ввода"""
        print("\n--- Добавление новой реки ---")
        name = validator.safe_input("Введите название реки: ", "Название реки")
        volume = validator.safe_input("Введите объем (м³): ", "Объем", 'float')
        fill_time = validator.safe_input("Введите время наполнения (ч): ", "Время наполнения", 'float')
        creation_year = validator.safe_input("Введите год создания: ", "Год создания", 'date')
        length = validator.safe_input("Введите длину реки: ", "Длина реки", 'float')
        
        return cls(name, volume, fill_time, creation_year, length)
    
    def to_file_format(self):
        """Возвращает строку для сохранения в файл"""
        return f'река "{self.name}" {self.volume} {self.fill_time} {self.creation_year} {self.length}'