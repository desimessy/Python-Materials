# Въвеждане на параметрите на уравнението:
a,b=eval(input("Въведете (чрез запетая) две числа: "))
# Ако параметрите са некоректни:
if (type(a)!=int and type(a)!=float) or (type(b)!=int and type(b)!=float):
    print("Въведените стойности са некоректни!")
    # Край на изпълнението на програмата:
    raise SystemExit(0)
# Ако първият параметър е ненулев:
elif a!=0:
    txt="Решение x="+str(b/a)
# Ако вторият параметър е ненулев (при нулев първи):
elif b!=0:
    txt="Няма решение!"
# Ако и двата параметъра са нулеви:
else:
    txt="Решение - всяко число!"
# Вид на уравнението:
print("Уравнение "+str(a)+"x="+str(b))
# Резултат от търсенето на корена:
print(txt)
print("Търсенето на решение приключи.")
