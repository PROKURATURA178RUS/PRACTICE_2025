from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor 
import time

class CPU:

    def sum_of_squares(self, piece):
        return sum(x**2 for x in piece)
    
    def CPU_bound(self):
            numbers = list(range(1, 1000001)) 
            num_workers = 4 # Количество потоков
            piece_size = len(numbers) // num_workers # Определения размера каждой части разделенного numbers
            pieces = [numbers[i*piece_size:(i+1)*piece_size] for i in range(num_workers)] # Разделение numbers на части для параллельного выполнения

            # Потоки
            start_time = time.perf_counter() # Запись времени
            with ThreadPoolExecutor(max_workers=num_workers) as exec:
                partial_sums = list(exec.map(self.sum_of_squares, pieces)) # Выполняем sum_of_squares параллельно для каждой части pieces с использованием пула потоков. Сохраняем результаты в partial_sums
            total_sum_threads = sum(partial_sums) # Суммирование всех результатов
            end_time = time.perf_counter() # Измерение времени
            print(f"Потоки: {end_time - start_time:.2f} секунд, сумма: {total_sum_threads}")
            
            # Процессы
            start_time = time.perf_counter()
            with ProcessPoolExecutor(max_workers=num_workers) as exec:
                partial_sums = list(exec.map(self.sum_of_squares, pieces)) 
            total_sum_processes = sum(partial_sums)
            end_time = time.perf_counter()
            print(f"Процессы: {end_time - start_time:.2f} секунд, сумма: {total_sum_processes}") # Практически идентичная часть кода, только для процессов