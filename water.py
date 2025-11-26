from data_validator import DataValidator

class Water:
    """Базовый класс для водных объектов"""
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def create_from_input(cls, validator):
        """Базовый метод для создания объекта из пользовательского ввода"""
        raise NotImplementedError("Метод должен быть реализован в подклассе")