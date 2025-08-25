from data_engine import DataEngine

def main():
    filename = "var5.csv"
    if DataEngine.process_data(filename):
        # Дальнейшая обработка данных
        pass
    else:
        print("Обработка файла прервана из-за ошибок")

if __name__ == "__main__":
    main() 