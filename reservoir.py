from water import Water

class Reservoir(Water):
    """Класс для водохранилищ"""
    def __init__(self, name, length, water_flow):
        super().__init__(name)
        self.length = length
        self.water_flow = water_flow
    
    @classmethod
    def create_from_input(cls, validator):
        """Создает водохранилище из пользовательского ввода"""
        print("\n--- Добавление нового водохранилища ---")
        name = validator.safe_input("Введите название водохранилища: ", "Название водохранилища")
        length = validator.safe_input("Введите длину (км): ", "Длина", 'float')
        water_flow = input("Введите расход воды: ")
        
        return cls(name, length, water_flow)
    
    def to_file_format(self):
        """Возвращает строку для сохранения в файл"""
        return f'водохранилище "{self.name}" {self.length} {self.water_flow}'