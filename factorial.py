#python program on factoria
factorial = 1
n=int(input("NUMBER:"))
if n < 0:
	print("the number is less than 0")
elif n == 0:
	print("the factorial of 0 is 1")
else:
	for i in range(1,n+1):
		factorial = factorial*i
	print("factorial of",n,"is",factorial)
