class CaesarCipher:
    def __init__(self, input_text, shift):
        self.input_text = input_text
        self.shift = shift
    
    def encrypt(self):
        """Шифрование текста методом Цезаря"""
        result = ""
        for char in self.input_text:
            if char.isalpha():
                # Определяем базовый символ в зависимости от регистра
                base = ord('A') if char.isupper() else ord('a')
                # Сдвигаем символ и обеспечиваем циклическое перемещение
                shifted_char = chr((ord(char) - base + self.shift) % 26 + base)
                result += shifted_char
            else:
                # Не-буквенные символы остаются без изменений
                result += char
        return result
    
    def decrypt(self):
        """Расшифровка текста, зашифрованного методом Цезаря"""
        result = ""
        for char in self.input_text:
            if char.isalpha():
                # Определяем базовый символ в зависимости от регистра
                base = ord('A') if char.isupper() else ord('a')
                # Сдвигаем символ в обратную сторону
                shifted_char = chr((ord(char) - base - self.shift) % 26 + base)
                result += shifted_char
            else:
                # Не-буквенные символы остаются без изменений
                result += char
        return result


class VernamCipher(CaesarCipher):
    def __init__(self, input_text, shift, key_word):
        # Вызываем конструктор родительского класса
        super().__init__(input_text, shift)
        self.key_word = key_word
    
    def encrypt(self):
        """Шифрование текста методом Вернама"""
        # Преобразуем ключ к верхнему регистру для единообразия
        key = self.key_word.upper()
        encrypted_text = ""
        key_index = 0
        
        for char in self.input_text:
            if char.isalpha():
                # Определяем базовый символ в зависимости от регистра
                base = ord('A') if char.isupper() else ord('a')
                # Получаем числовое представление символа и ключа
                char_num = ord(char.upper()) - ord('A')
                key_num = ord(key[key_index % len(key)]) - ord('A')
                
                # Применяем операцию XOR и модуль 26
                encrypted_num = (char_num ^ key_num) % 26
                encrypted_char = chr(encrypted_num + base)
                
                encrypted_text += encrypted_char
                key_index += 1
            else:
                # Не-буквенные символы остаются без изменений
                encrypted_text += char
        
        return encrypted_text
    
    def decrypt(self):
        """Расшифровка текста, зашифрованного методом Вернама"""
        # Для шифра Вернама процедура расшифровки идентична шифрованию
        return self.encrypt()


# Демонстрация работы классов
if __name__ == "__main__":
    # Пример использования шифра Цезаря
    caesar = CaesarCipher("Hello, World!", 3)
    encrypted_caesar = caesar.encrypt()
    decrypted_caesar = caesar.decrypt()
    
    print("Шифр Цезаря:")
    print(f"Исходный текст: Hello, World!")
    print(f"Зашифрованный: {encrypted_caesar}")
    print(f"Расшифрованный: {decrypted_caesar}")
    print()
    
    # Пример использования шифра Вернама
    vernam = VernamCipher("Secret Message", 0, "KEY")
    encrypted_vernam = vernam.encrypt()
    decrypted_vernam = vernam.decrypt()
    
    print("Шифр Вернама:")
    print(f"Исходный текст: Secret Message")
    print(f"Зашифрованный: {encrypted_vernam}")
    print(f"Расшифрованный: {decrypted_vernam}")