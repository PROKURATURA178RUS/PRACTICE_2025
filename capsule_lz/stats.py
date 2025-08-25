import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from decorators import log_decorator

class GraphicsStatistics:
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    @log_decorator
    def show_histogram(self, column_name, title="Гистограмма", xlabel="Значения", ylabel="Частота"):
        """Отображает гистограмму для указанного столбца"""
        plt.figure(figsize=(10, 6))
        plt.hist(self.dataframe[column_name].dropna(), bins=20, alpha=0.7, color='skyblue', edgecolor='black')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(axis='y', alpha=0.75)
        plt.show()
    
    @log_decorator
    def show_heatmap(self, columns=None, title="Тепловая карта корреляций"):
        """Отображает тепловую карту корреляций"""
        if columns is None:
            # Используем все числовые колонки
            numeric_df = self.dataframe.select_dtypes(include=['number'])
        else:
            numeric_df = self.dataframe[columns]
        
        # Вычисляем корреляционную матрицу
        corr_matrix = numeric_df.corr()
        
        plt.figure(figsize=(12, 8))
        sns.heatmap(corr_matrix, 
                   annot=True, 
                   cmap='coolwarm', 
                   center=0,
                   square=True,
                   fmt='.2f',
                   cbar_kws={"shrink": .8})
        plt.title(title)
        plt.tight_layout()
        plt.show()
    
    @log_decorator
    def show_player_statistics(self):
        """Специальный метод для отображения статистики игроков по странам"""
        # Предполагаем, что в данных есть колонки с названиями стран
        # Найдем колонки, которые могут содержать данные о игроках
        country_columns = ['Россия', 'США', 'Китай', 'Франция']
        
        # Проверим, какие колонки действительно есть в данных
        available_countries = [col for col in country_columns if col in self.dataframe.columns]
        
        if not available_countries:
            print("Колонки с данными по странам не найдены")
            return
        
        # Создаем данные для графика
        player_data = []
        for country in available_countries:
            # Предполагаем, что данные в сотнях тысяч
            total_players = self.dataframe[country].sum() / 10  # Конвертируем в сотни тысяч
            player_data.append(total_players)
        
        # Создаем гистограмму
        plt.figure(figsize=(12, 8))
        bars = plt.bar(available_countries, player_data, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
        
        plt.title('Количество игроков Steam по странам\n(в сотнях тысяч)', fontsize=16, fontweight='bold')
        plt.xlabel('Страны', fontsize=12)
        plt.ylabel('Количество игроков (сотни тысяч)', fontsize=12)
        
        # Добавляем значения на столбцы
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{height:.1f}', ha='center', va='bottom', fontweight='bold')
        
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.show()