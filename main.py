import math


a = float(input("Коэффициент а = "))
b = float(input("Коэффициент b = "))
c = float(input("Коэффициент c = "))


def formula(a,b,c):
	d = b**2 - 4*a*c
	if d>0:
		x1 = (-b + math.sqrt(d))/2/a
		x2 = (-b - math.sqrt(d))/2/a
		print("Корни уравнения:",x1,x2)
	elif d==0:
		x = -b/2/a
		print("Корень уравнения:",x)
	else: print("Корней нет")
	
	
	
formula(a,b,c)
