import asyncio
from times import SQUARE
from cpu import CPU
from except_async import EXCEPT

def main():
    cpu = CPU()
    except_asynchronous = EXCEPT()
    ThreadPoolExecutor = SQUARE()
    while True:
        print("Выберите, что хотите проверить.")
        print("1. Пул потоков")
        print("2. Сравнение производительности: процессы vs потоки")
        print("3. Обработка исключений")
        choice = input("Ваш выбор?: ")
        
        if choice == '1':
            try:
                ThreadPoolExecutor.square()
            except Exception as e:
                print(f"Произошла ошибка в Задаче 1: {e}")
        elif choice == '2':
            try:
                cpu.CPU_bound()
            except Exception as e:
                print(f"Произошла ошибка в Задаче 2: {e}")
        elif choice == '3':
            try:
                asyncio.run(except_asynchronous.except_())
            except Exception as e:
                print(f"Произошла ошибка в Задаче 3: {e}")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()