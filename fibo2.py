n = input('enter the number:')
x=0
y=1
print str(x)
print str(y)
for x in range(n-2):
	z=x+y
	print str(z)
	x=y
	y=z

