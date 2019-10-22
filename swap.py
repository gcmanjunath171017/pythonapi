def swap(a, b):
    print "Before swap %s, %s" %(a, b)
    if a != b:
        a, b = b, a
    print "After swap %s, %s" %(a, b)

x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))
swap(x,y)

def swap(a, b):
    if a != b:
        #a, b = b, a
        return b, a
    else:
        return a, b

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print "Before swap %s, %s" %(a, b)
a, b = swap(a, b)
print "After swap %s, %s" %(a, b)


a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print "Before swap %s, %s" %(a, b)
a, b = (b, a) if a!=b else (a,b)
print "After swap %s, %s" %(a, b)
