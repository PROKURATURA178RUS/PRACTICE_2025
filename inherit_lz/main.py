from ciphers import CaesarCipher, VernamCipher

# Пример использования
caesar = CaesarCipher("Example Text", 5)
print(caesar.encrypt())

vernam = VernamCipher("Secret Message", 0, "KEYWORD")
print(vernam.encrypt())