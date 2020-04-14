# This is Calculater Project 
from time import sleep
def calc():
    add      =  lambda x,y : x + y
    subtract =  lambda x,y : x - y
    multiply =  lambda x,y : x * y
    divide   =  lambda x,y : x / y

    print("""\n           Choose Wht u Want\n
    1 : Add             2 : Subtract
    3 : Multiply        4 : Divide\n""".upper())

    choose = input("enter your choose no. :   ")

    num1 = int(input("enter no. 1  :  "))
    num2 = int(input("enter no. 2  :  "))

    if (choose == '1'):
        print("add 2 no. is : ", add(num1,num2))
    elif (choose == '2'):
        print("Subtract 2 no. is : ", subtract(num1,num2))
    elif (choose == '3'):
        print("multiply 2 no. is : ", multiply(num1,num2))
    elif (choose == '4'):
        print("divide 2 no. is : ", divide(num1,num2))

calc()
sleep(1)
print("""Thanks for using
Now u exit the Prog. """)
