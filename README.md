# python-
quadratic equation
j=int(input("Wie viele Gleichung hast du? "))
i =1
while i<=j :
	print("Gleichung Nummer= ",i)
	print(".                                        		                 ax^2+pX+q")
	print("																					Quadratische Gleichungenrechnerisches Lösen")
	a= float(input("Eingeben a= "))
	p= float(input("Eingeben p= "))
	q= float(input("Eingeben q= "))
	print("																												X1=")
	print("																												X2=")
	p1=float(p/(2*a))
	p2=float(p*p)
	delta=float(p2-4*a*q)
	if delta < 0 :
		print("delta ",delta)
		print("Keine Lösung")
	else :
		import math
		delta1=float(math.sqrt(delta))
		x1=float(-p1+(delta1/(2*a)))
		x2=float(-p1-(delta1/(2*a)))
		print("X1= ",x1)
		print("X2= ",x2)
	i=i+1
print("Ende")
