from octagon import Octagon

# Создание объекта октагона
octagon = Octagon(5)

# Вывод параметров
print(f"Площадь октагона: {octagon.area():.3f}")
print(f"Периметр октагона: {octagon.perimeter():.3f}")

# Отрисовка фигур
octagon.draw()