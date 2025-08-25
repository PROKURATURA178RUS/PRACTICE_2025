import time
from concurrent.futures import ThreadPoolExecutor

class SQUARE:
    def square(self):
        numbers = list(range(1, 1000001)) # Создание списка в миллион значений
        
        # Без использования потоков
        start_time = time.perf_counter() # Запись времени
        squares = [x**2 for x in numbers]
        end_time = time.perf_counter() # Измерение времени
        print(f"Без потоков: {end_time - start_time:.2f} секунд")
        
        # С использованием потоков
        def calculate_square(x):
            return x**2
        
        start_time = time.perf_counter()
        with ThreadPoolExecutor(max_workers=10) as exec:
            squares = list(exec.map(calculate_square, numbers))
        end_time = time.perf_counter()
        print(f"С 10 потоками: {end_time - start_time:.2f} секунд") # Аналогичный кодс использованием потоков