# Прочитане на текстовите стойности:
text=input("Първи текст: ")
# Първо множество:
A=set(text)
text=input("Втори текст: ")
# Второ множество:
B=set(text)
# Общите букви:
C=A&B
# Резултат:
print("Буквите от първия текст: ",A)
print("Буквите от втория текст: ",B)
print("Общите букви: ",C)
