
import math
print(""" Enter the operators:
1. ADDITION
2.SUBTRACTION
3.MULTIPLICATION
4.DIVISION
5.EXPONENTIAL OPERATOR
6.SIN FUNCTION
7.COS FUNCTION
8.SQUARE ROOT
9.SQUARE OF A NUMBER
10.LOG
0.EXIT CALCULATOR\n\n""")
while True:
    choice=int(input("Enter your choice(1,2,3,4,5,6,7,8,9,0)\n\n"))
    if choice==0:
        exit()
    if choice in range(1, 6):
        num1 = float(input("Enter The 1st Number-"))
        num2 = float(input("Enter The 2nd Number-"))
    elif choice in range(6, 8):
           num = float(input("Enter the value_"))
           x = input("Answer in Radian or Degree--")
    else:
       num3 = float(input("Enter The Number -"))
    if choice == 1:
      print(num1, '+', num2, '=', num1+num2)
    if choice == 2:
      print(num1, '-', num2, '=', num1- num2)
    if choice == 3:
      print(num1, '*', num2, '=', num1 * num2)
    if choice == 4:
      print(num1, '/', num2, '=', num1/num2)
    if choice == 5:
      print(num1, '**', num2, '=', num1**num2)
    if choice==8:
        print("Square Root Of Number is=",math.sqrt(num3))
    if choice==9:
        print("Square Of Number is=",num3**num3 )
    if choice == 6:
        if x=="radian":
            print("Sin function of", num, 'in radian =', math.sin(num))
        else:
            print("Sin function in Degrees is=",round(math.sin(math.radians(x)),1))
    if choice==7:
        if x == "radian":
            print("Cos function of", num, 'in radian =',math.cos(num))
        else:
            print("Cos function in Degrees is=",round(math.cos(math.radians(num)),1))
    if choice==10:
        print(" log of",num3,"is",math.log10(num3))