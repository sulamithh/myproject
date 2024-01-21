# file = open("test.txt", "r")

try:
    file = open("test.txt", "r")

except FileNotFoundError:
    print("Вы пытаетесь открыть и прочитать несуществующий файл!")

else:
    print("Ошибки нет")
finally:
    print("Блок finally выполнен")