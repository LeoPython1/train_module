

def math_addition(a, b, c):
    return a + b + c

def math_y(a, b):
    return a * b 

def fun_math(a):
    if a > 0:
        print(f"{a} положительное!")

    if a < 0:
        print(f"{a} отрицательное!")

    if a == 0:
        print(f"{a} это как-ты, 0!")

def user_math():
    user = input("Ты давай-ка лентяй введи число, быстро! Ввод: ")
    user = int(user)
    fun_math(user)




math = math_addition(7871329872193, 7123971294682374, 182574623874782637216845217386126457)
math_v2 = math_y(213213422, 3091280371948)


print(math_v2)
print(math_y(988278424, 1231232356))
print(fun_math(0))
print(user_math())