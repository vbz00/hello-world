class fib(object):
	'''create class fib'''

	def __init__(self, n):
		self.n=n

	def print_ser(self):
		'''Creates print _setyfugries method'''
		#=input("Enter the no. of terms - ")
		x=0
		y=1
		print x
		print y
		for x in range(self.n-2):
			z=x+y
			print z
			x=y
			y=z
	def print_hello(self):
		'''prints greetings'''
		print 'Hello, welcome to python'
	
	def print_py(self):
		for i in range(self.n):
			for j in range(i):
				print(j+1)
			print
		for k in range(n,0,-1):
			for i in range(k):
				print l+1
				print

	def print_all(self):

		self.print_ser()
		self.print_hello()
		self.print_py()


