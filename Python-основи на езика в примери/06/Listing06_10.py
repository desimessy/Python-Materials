# Във функцията се използват локални и глобални променливи:
def myfunction():
    # Глобални променливи:
    global A,B
    # Присвояване на стойности на променливите:
    A="Алфа"
    B="Браво"
    D="Делта"
    # Проверка на стойностите:
    print("Във функцията: A =",A)
    print("Във функцията: B =",B)
    print("Във функцията: C =",C)
    print("Във функцията: D =",D)
# Глобални променливи:
A="Alpha"
C="Charlie"
D="Delta"
# Проверка на стойностите на променливите:
print("До извикване на функцията: A =",A)
print("До извикване на функцията: C =",C)
print("До извикване на функцията: D =",D)
# Извикване на функцията:
myfunction()
# Проверка на стойностите на променливите:
print("След извикване на функцията: A =",A)
print("След извикване на функцията: B =",B)
print("След извикване на функцията: C =",C)
print("След извикване на функцията: D =",D)
