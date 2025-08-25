from data_engine import DataEngine

def main():
    # Создаем обработчик данных
    engine = DataEngine('var5.csv')
    
    # Загружаем данные
    engine.load_data()
    
    # Удаляем дубликаты с помощью унарного оператора
    engine = ~engine
    
    # Разделяем данные по городу и сохраняем
    engine.split_by_city()
    
    # Выводим информацию о данных
    print("\nИнформация о данных:")
    print(engine.get_info())

if __name__ == "__main__":
    main()