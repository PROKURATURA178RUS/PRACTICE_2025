import pandas as pd
import numpy as np

class DataEngine:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.removed_duplicates_count = 0
    
    def load_data(self):
        """Загрузка данных из CSV файла"""
        self.df = pd.read_csv(self.file_path)
        print(f"Данные загружены. Размер: {self.df.shape}")
        return self
    
    def split_by_city(self):
        """Разделение данных по признаку 'Место ответа' на Минск и другие города"""
        if self.df is None:
            raise ValueError("Данные не загружены. Сначала вызовите load_data()")
        
        # Создаем датафрейм для Минска
        minsk_df = self.df[self.df['Место ответа'] == 'Минск'].copy()
        minsk_filename = "Минск.csv"
        minsk_df.to_csv(minsk_filename, index=False, encoding='utf-8-sig')
        print(f"Сохранен файл: {minsk_filename} с {len(minsk_df)} записями")
        
        # Создаем датафрейм для других городов
        other_cities_df = self.df[self.df['Место ответа'] != 'Минск'].copy()
        other_cities_filename = "Другие_города.csv"
        other_cities_df.to_csv(other_cities_filename, index=False, encoding='utf-8-sig')
        print(f"Сохранен файл: {other_cities_filename} с {len(other_cities_df)} записями")
        
        return self
    
    def __invert__(self):
        """Унарный оператор ~ для удаления дубликатов"""
        if self.df is None:
            raise ValueError("Данные не загружены. Сначала вызовите load_data()")
        
        # Сохраняем исходное количество строк
        original_count = len(self.df)
        
        # Удаляем дубликаты
        self.df = self.df.drop_duplicates()
        
        # Вычисляем количество удаленных дубликатов
        self.removed_duplicates_count = original_count - len(self.df)
        print(f"Количество удаленных дубликатов: {self.removed_duplicates_count}")
        
        return self
    
    def get_info(self):
        """Получение информации о данных"""
        if self.df is None:
            return "Данные не загружены"
        
        info = f"Размер данных: {self.df.shape}\n"
        info += f"Колонки: {list(self.df.columns)}\n"
        
        if 'Место ответа' in self.df.columns:
            cities = self.df['Место ответа'].unique()
            info += f"Города: {cities}\n"
        
        info += f"Удалено дубликатов: {self.removed_duplicates_count}"
        
        return info