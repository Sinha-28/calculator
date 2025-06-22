print("welcome to calculator")
X=float(input("enter first number"))
Y=float(input("enter second number"))
Z=input("enter \n1:SUM\n2:SUB\n3:MUL\n4:DIV\n")
# print("\n")
if (Z=="1"):
    
    print("sum of numbers are",X+Y)
elif Z=="2":
    print("subtract of numbers are",X-Y)
elif Z=="3":
    print("multiply of numbers are",X*Y)
elif Z=="4":
    print("divide of numbers are",X//Y)
else:
    print("wrong input")