import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

class Octagon:
    def __init__(self, side):
        self.side = side
        self.angle = 135  # Внутренний угол октагона в градусах
        self.k = 1 + math.sqrt(2)  # Константа k
    
    def circumscribed_circle_radius(self):
        """Радиус описанной окружности"""
        return self.side * math.sqrt(1 + 1/math.sqrt(2))
    
    def circumscribed_circle_area(self):
        """Площадь описанной окружности"""
        return math.pi * (self.circumscribed_circle_radius() ** 2)
    
    def inscribed_circle_radius(self):
        """Радиус вписанной окружности"""
        return self.side * (1 + math.sqrt(2)) / 2
    
    def inscribed_circle_area(self):
        """Площадь вписанной окружности"""
        return math.pi * (self.inscribed_circle_radius() ** 2)
    
    def area(self):
        """Площадь октагона"""
        return 2 * (1 + math.sqrt(2)) * self.side ** 2
    
    def perimeter(self):
        """Периметр октагона"""
        return 8 * self.side
    
    def draw(self):
        """Отрисовка фигур на координатной плоскости"""
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_aspect('equal')
        
        # Центр фигур
        center_x, center_y = 0, 0
        
        # Описанная окружность
        circum_radius = self.circumscribed_circle_radius()
        circum_circle = patches.Circle((center_x, center_y), circum_radius, 
                                      fill=False, edgecolor='red', linewidth=2, label='Описанная окружность')
        ax.add_patch(circum_circle)
        
        # Вписанная окружность
        inscr_radius = self.inscribed_circle_radius()
        inscr_circle = patches.Circle((center_x, center_y), inscr_radius, 
                                     fill=False, edgecolor='green', linewidth=2, label='Вписанная окружность')
        ax.add_patch(inscr_circle)
        
        # Октагон
        octagon_points = []
        for i in range(8):
            angle_rad = math.radians(i * 45 - 22.5)  # Смещение на 22.5° для правильной ориентации
            x = center_x + circum_radius * math.cos(angle_rad)
            y = center_y + circum_radius * math.sin(angle_rad)
            octagon_points.append((x, y))
        
        octagon = patches.Polygon(octagon_points, closed=True, 
                                 fill=False, edgecolor='blue', linewidth=3, label='Октагон')
        ax.add_patch(octagon)
        
        # Настройка графика
        limit = circum_radius * 1.2
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        ax.set_title('Октагон с вписанной и описанной окружностями')
        ax.legend(loc='upper right')
        plt.show()
