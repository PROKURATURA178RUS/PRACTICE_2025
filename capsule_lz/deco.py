import pandas as pd
import getpass
from datetime import datetime
import functools

def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Собираем информацию для лога
        log_data = {
            'id': id(func),
            'pc username': getpass.getuser(),
            'function name': func.__name__,
            'Date': datetime.now().strftime("%d.%m.%Y"),
            'Time': datetime.now().strftime("%H:%M:%S")
        }
        
        # Преобразуем в DataFrame
        log_df = pd.DataFrame([log_data])
        
        # Записываем в файл
        try:
            # Пытаемся прочитать существующий файл
            existing_df = pd.read_csv('logs.csv')
            updated_df = pd.concat([existing_df, log_df], ignore_index=True)
            updated_df.to_csv('logs.csv', index=False)
        except FileNotFoundError:
            # Если файла нет, создаем новый
            log_df.to_csv('logs.csv', index=False)
        
        # Вызываем оригинальную функцию
        return func(*args, **kwargs)
    return wrapper