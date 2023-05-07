import time
import random
import os

def start_game():
    time.sleep(2)
    print("1.")
    game_program = random.randint(1,3)
    input_program = input("Я загадал число! Угадай его! Ввод: ")

    input_program = int(input_program)

    while input_program not in [1, 2, 3]:
        print("Здесь можно вводить числа только от 1 до 3!")
        input_program = input("Ввод: ")
        input_program = int(input_program)

    if game_program != input_program:
        print("Ты не угадал!")

    if game_program == input_program:
        print("Ты угадал!")

    

print("Привет! В этой игре ты должен угадать моё число от 1 до 3! Погнали играть,лентяй!")

def continue_game():
    print("2.")
    print("Будешь играть ещё?")
    repeat = input("Ввод: ")
    repeat = repeat.lower()
    
    if repeat.startswith(("y", "д")):
        return True

    if repeat.startswith(("n", "н")):
        print("Ну ладно, КРАКАЗЯБРА!")
        return False
    
    else:
        print("Извиви, друг мой, но так нельзя!")
        return continue_game()
        
#["No", "Не", "Нет", "Не хочу", "Не буду"]
def game():
    print("3.")
    is_playing = True
    while is_playing:
        start_game()
        is_playing = continue_game()

game()