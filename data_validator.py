class DataValidator:
    """Класс для валидации данных"""
    
    @staticmethod
    def validate_float(value, field_name):
        """Валидация числовых значений"""
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"{field_name} должно быть числом")
    
    @staticmethod
    def validate_string(value, field_name):
        """Валидация строковых значений"""
        if not value or not value.strip():
            raise ValueError(f"{field_name} не может быть пустым")
        return value.strip()
    
    @staticmethod
    def validate_date(value, field_name):
        """Простая валидация даты"""
        if not value or not value.strip():
            raise ValueError(f"{field_name} не может быть пустой")
        
        if '-' in value:
            raise ValueError(f"{field_name} не может быть отрицательной")
        
        return value.strip()
    
    @staticmethod
    def safe_input(prompt, field_name, validation_type='string'):
        """Безопасный ввод с валидацией"""
        while True:
            try:
                value = input(prompt)
                if validation_type == 'float':
                    return DataValidator.validate_float(value, field_name)
                elif validation_type == 'date':
                    return DataValidator.validate_date(value, field_name)
                else:
                    return DataValidator.validate_string(value, field_name)
            except ValueError as e:
                print(f"Ошибка: {e}")