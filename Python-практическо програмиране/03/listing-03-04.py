print("*" * 15, " Калкулатор ", "*" * 10)
print("За изход въведете q в качеството на знак за операция")
while True:
	s = input("Знак (+,-,*,/): ")
	if s == 'q': break
	if s in ('+','-','*','/'):
		x = float(input("x="))
		y = float(input("y="))
		if s == '+':
			print("%.2f" % (x+y))
		elif s == '-':
			print("%.2f" % (x-y))
		elif s == '*':
			print("%.2f" % (x*y))
		elif s == '/':
			if y != 0:
				print("%.2f" % (x/y))
			else:
				print("Деление на нула!")
	else:
		print("Недопустим знак за операция!")
