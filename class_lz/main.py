from octagon import Octagon #Импортируем класс

def main(): #Создаем функцию 
    first = Octagon(8) #Добавляем объект
    first.plo() #Используем все имеющиеся методы
    first.per()
    first.opis_okr()
    first.vpis_okr()
    first.pic()

if __name__ == '__main__': 
    main() 