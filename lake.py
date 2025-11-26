from water import Water

class Lake(Water):
    """Класс для озер"""
    def __init__(self, name, depth, width):
        super().__init__(name)
        self.depth = depth
        self.width = width
    
    @classmethod
    def create_from_input(cls, validator):
        """Создает озеро из пользовательского ввода"""
        print("\n--- Добавление нового озера ---")
        name = validator.safe_input("Введите название озера: ", "Название озера")
        depth = validator.safe_input("Введите глубину (м): ", "Глубина", 'float')
        width = validator.safe_input("Введите ширину (м): ", "Ширина", 'float')
        
        return cls(name, depth, width)
    
    def to_file_format(self):
        """Возвращает строку для сохранения в файл"""
        return f'озеро "{self.name}" {self.depth} {self.width}'