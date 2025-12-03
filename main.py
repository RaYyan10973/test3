from program import Program





def display_all_data(program):
    """Вывод всех данных"""
    if not program.objects:
        print("📭 Нет данных для отображения")
        return
    
    # Получаем объекты по типам
    lakes = program.get_objects_by_type('lake')
    seas = program.get_objects_by_type('sea')
    rivers = program.get_objects_by_type('river')
    reservoirs = program.get_objects_by_type('reservoir')
    
    # Выводим моря
    print("=" * 50)
    print("МОРЯ")
    print("=" * 50)
    if seas:
        for sea in seas:
            print(f"Название: {sea.name}")
            print(f"  Глубина: {sea.depth} м")
            print(f"  Соленость: {sea.salinity} ‰")
            print("-" * 30)
    else:
        print("Моря не найдены")
    
    # Выводим озера
    print("\n" + "=" * 50)
    print("ОЗЕРА")
    print("=" * 50)
    if lakes:
        for lake in lakes:
            print(f"Название: {lake.name}")
            print(f"  Глубина: {lake.depth} м")
            print(f"  Ширина: {lake.width} м")
            print("-" * 30)
    else:
        print("Озера не найдены")
    
    # Выводим реки
    print("\n" + "=" * 50)
    print("РЕКИ")
    print("=" * 50)
    if rivers:
        for river in rivers:
            print(f"Название: {river.name}")
            print(f"  Объем: {river.volume} м³")
            print(f"  Время наполнения: {river.fill_time} ч")
            print(f"  Год создания: {river.creation_year}")
            print(f"  Длина реки: {river.length}")
            print("-" * 30)
    else:
        print("Реки не найдены")
    
    # Выводим водохранилища
    print("\n" + "=" * 50)
    print("ВОДОХРАНИЛИЩА")
    print("=" * 50)
    if reservoirs:
        for reservoir in reservoirs:
            print(f"Название: {reservoir.name}")
            print(f"  Длина: {reservoir.length} км")
            print(f"  Расход воды: {reservoir.water_flow}")
            print("-" * 30)
    else:
        print("Водохранилища не найдены")


def show_menu():
    """Главное меню"""
    program = Program()
    
    while True:
        print("\n" + "=" * 50)
        print(" СИСТЕМА УПРАВЛЕНИЯ ВОДНЫМИ ОБЪЕКТАМИ")
        print("=" * 50)
        print("1 - Загрузить данные из файла")
        print("2 - Просмотреть все данные")
        print("3 - Добавить новое озеро")
        print("4 - Добавить новое море")
        print("5 - Добавить новую реку")
        print("6 - Добавить новое водохранилище")
        print("7 - Показать статистику")
        print("0 - Выход")
        print("-" * 50)
        
        choice = input("Выберите действие: ").strip()
        
        if choice == '1':
            program.load_from_file()
        elif choice == '2':
            display_all_data(program)
        elif choice == '3':
            program.add_object_from_input('lake')
        elif choice == '4':
            program.add_object_from_input('sea')
        elif choice == '5':
            program.add_object_from_input('river')
        elif choice == '6':
            program.add_object_from_input('reservoir')
        elif choice == '7':
            stats = program.get_statistics()
            print(f"\n СТАТИСТИКА:")
            print(f"     Озера: {stats['lakes']}")
            print(f"    Моря: {stats['seas']}")
            print(f"     Реки: {stats['rivers']}")
            print(f"    Водохранилища: {stats['reservoirs']}")
            print(f"    Всего объектов: {stats['total']}")
        elif choice == '0':
            print("👋 Выход из программы...")
            break
        else:
            print(" Неверный выбор! Попробуйте снова.")


def main():
    """Точка входа в программу"""
    print(" ЗАПУСК СИСТЕМЫ УПРАВЛЕНИЯ ВОДНЫМИ ОБЪЕКТАМИ")
    print("=" * 55)
    
    try:
        show_menu()
    except KeyboardInterrupt:
        print("\n\n Программа прервана пользователем")
    except Exception as e:
        print(f"\n\n Критическая ошибка: {e}")
    finally:
        print("\n Программа завершена")


if __name__ == "__main__":
    main()