# Прочитане на числото:
number=int(input("Въведете число: "))
# Ако числото е отрицателно:
if number<0:
    number*=-1
# Създава се празно множество:
digits=set()
# Ако е въведена нула:
if number==0:
    digits.add(0)
# Ако числото не е равно на нула:
else:
    # Обхождане на цифрите в представянето на числото:
    while number!=0:
        # Последната цифра в представянето на числото:
        digits.add(number%10)
        # В представянето на числото се отхвърля
        # последната цифра:
        number//=10
print("Числото се състои от следните цифри:")
# Показване на резултата:
for n in digits:
    print(n,end=" ")
# Преминаване на нов ред:
print()
