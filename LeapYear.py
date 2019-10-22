num=int(input("Enter the Year:"))
if num > 0:
	if (num % 4) == 0:
		if(num % 100) == 0:
			if(num % 400) == 0:
				print("{0} is a Leap Year".format(num))
			else:
				print("{0} is not a Leap Year".format(num))	
		else:
			print("{0} is a Leap Year".format(num))
	else:
		print("{0} is not a Leap Year".format(num))
else:
		print("Enter Valid Year")
