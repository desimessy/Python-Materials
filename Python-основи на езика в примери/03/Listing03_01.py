# Различни начини за създаване на кортежи:
Alpha=(5,10,15,"двайсет")
Bravo=100,["едно","две","три"],200
Charlie=tuple([1,2,3,(4,5,6,7,8,9)])
Delta=tuple("ABCDEF")
Echo=tuple(2**k for k in range(11))
# Прочитане стойностите на елементите и получаване на срез:
print("Alpha:",Alpha)
print("Елементи:",len(Alpha))
print("Първи:",Alpha[0])
print("Последен:",Alpha[-1])
print("Bravo:",Bravo)
print("Елементи:",len(Bravo))
print("Bravo[1]:",Bravo[1])
print("Bravo[1][2]:",Bravo[1][2])
print("Charlie:",Charlie)
print("Елементи:",len(Charlie))
print("Charlie[3]:",Charlie[3])
print("Charlie[3][1:4]:",Charlie[3][1:4])
print("Delta:",Delta)
print("Елементи:",len(Delta))
print("Delta[-3:]:",Delta[-3:])
print("Echo:",Echo)
Foxtrot=tuple(Echo[k] for k in range(len(Echo)) if k%2==0)
print("Foxtrot:",Foxtrot)
Golf=Echo[2:5]
print("Golf:",Golf)
