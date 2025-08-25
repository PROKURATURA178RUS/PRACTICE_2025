import asyncio
import random

class EXCEPT:
    async def except_(self):
        async def faulty_function():
            await asyncio.sleep(random.uniform(0, 3)) # Определение асинхронной функции, которая принимает рандомное время 0-3 сек
            raise ValueError("Произошла ошибка") # Вызов исключения
        
        try:                
            await faulty_function()
        except ValueError as e:
            print(f"Поймано исключение: {e}")