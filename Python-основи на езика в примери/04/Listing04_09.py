# Горна граница за числата:
n=50
# Множество на естествените числа:
E=set(range(1,n+1))
# Множество на числата, които се делят на 3:
A={s for s in E if s%3==0}
# Множество на числата, които се делят на 11:
B={s for s in E if s%11==0}
# Множество на числата, които се делят на 5:
C={s for s in E if s%5==0}
# Множество на числата, които се делят на 7:
D={s for s in E if s%7==0}
# Множество на числата, които се делят на 3 или 11,
# но не се делят на 5 и 7:
N=(A|B)-(C|D)
# Показване на резултата:
print(N)
