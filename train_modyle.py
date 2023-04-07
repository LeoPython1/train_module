import time

# выбор маршрута

def get_route():
    route = input("Укажите свой маршрут: ")
    route = int(route)
    

    if route < 1 or route > 99:
        print("Извените но, укажите номер маршрута от 01 до 99!")
        print()
        get_route()

get_route()