# Функции с документиране:
def show(txt):
    "Това е функция show() с един аргумент."
    print("Единствен аргумент:",txt)
def display(a,b):
    "Това е функция display() с два аргумента."
    print("[1] Първи аргумент:",a)
    print("[2] Втори аргумент:",b)
# Функция без документиране:
def hello():
    print("Привет на всички!")
# Извикване на функциите и проверка на документацията:
print(show.__doc__)
show("A")
print(display.__doc__)
display("B","C")
# Променлива, отнасяща се към функция:
f=show
# Извикване на функциите и проверка на документацията:
print(f.__doc__)
f("D")
# Нов текст за документация:
display.__doc__="Новият текст за display()"
# Проверка на резултата:
print(display.__doc__)
display("E","F")
# Документиране за функцията:
hello.__doc__="Функция hello()"
# Проверка на резултата:
print(hello.__doc__)
hello()
