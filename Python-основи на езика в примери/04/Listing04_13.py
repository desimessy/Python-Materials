# Изходен речник:
A={"Начален":1,"Среден":2,"Последен":3}
# Създаване на копие на речника:
B=dict(A)
C=A.copy()
# Създаване на речник на основата на речник:
D={k:v*10 for k,v in A.items()}
# Показване на резултата:
print("Създадени са речниците:")
print("A =",A)
print("B =",B)
print("C =",C)
print("D =",D)
# Изменение на изходния речник:
for k in A:
    A[k]*=100
# Показване на резултата:
print("След изменението на оригинала:")
print("A =",A)
print("B =",B)
print("C =",C)
print("D =",D)
