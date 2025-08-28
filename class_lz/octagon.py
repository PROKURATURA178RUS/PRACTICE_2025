#импортируем библиотеки
import math
import matplotlib.patches
import matplotlib.pyplot as plt


#Создаем класс
class Octagon:
    def __init__(self, a): 
        self.k = (1+math.sqrt(2))
        self.corner = 135
        self.a = a

    def plo(self): #Находим площадь октагона
        self.square = 2*self.k*self.a**2
        print(f'Площадь октагона {self.square}')

    def per(self): #Находим периметр октагона
        self.perim = 8*self.a
        print(f'Периметр октагона {self.perim}')

    def opis_okr(self): #Находим радиуc и площадь описанной окружности
        self.square = 2*self.k*self.a**2
        self.big_r = math.sqrt(self.square/2/math.sqrt(2))
        self.big_s = 3.14*self.big_r**2
        print(f'Радиус описанной окружности {self.big_r}')
        print(f'Площадь описанной окружности {self.big_s}')

    def vpis_okr(self): #Находим радиуc и площадь вписанной окружности
        self.square = 2*self.k*self.a**2
        self.small_r = math.sqrt(self.square/8/(math.sqrt(2)-1))
        self.small_s = 3.14*self.small_r**2
        print(f'Радиус вписанной окружности {self.small_r}')
        print(f'Площадь вписанной окружности {self.small_s}')
    
    def pic(self): #Выводим графики на экран
        self.square = 2*self.k*self.a**2
        self.small_r = math.sqrt(self.square/8/(math.sqrt(2)-1))
        self.big_r = math.sqrt(self.square/2/math.sqrt(2))

        plt.xlim(-20, 20)
        plt.ylim(-20, 20)
        plt.grid()
        axes = plt.gca()

        # Вершины октагона
        vertices = [(self.small_r, self.a/2), 
                    (self.small_r, -self.a/2),
                    (self.a/2, -self.small_r),
                    (-self.a/2, -self.small_r),
                    (-self.small_r, -self.a/2),
                    (-self.small_r, self.a/2), 
                    (-self.a/2, self.small_r), 
                    (self.a/2, self.small_r)]

        # Рисуем октагон
        polygon_1 = matplotlib.patches.Polygon(vertices, fill=False, color='green')

        # Добавляем окружности
        circle1 = matplotlib.patches.Circle((0, 0), radius=self.big_r, fill = False, color = 'red')  #Описанная окружность
        circle2 = matplotlib.patches.Circle((0, 0), radius=self.small_r, fill = False, color = 'black') #Вписанная окружность
        axes.add_patch(circle1)
        axes.add_patch(circle2)
        axes.add_patch(polygon_1)

        # Добавляем диагонали 
        for i in range(4):
            x1, y1 = vertices[i]
            x2, y2 = vertices[i+4]
            plt.plot([x1, x2], [y1, y2], color='blue') 

        plt.show()



    #Деструктор
    def __del__(self):
        print('Октагон удален')