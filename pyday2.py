'''int = int (input("Enter your marks:"))
if int >=90 and int<100 :
    print("Grade: O")       
elif int >= 80 and int<90 :
    print("Grade: A")   
elif int >= 65 and int<80:
    print("Grade: B")
elif int >= 35 and int<65:
    print("Grade : C")
elif int >35 and int<35 :
    print("Fail")
elif int >0 and int<100:
    print ("invalid Marks")
else:
    print("Invalid Marks")

int = int(input("Enter your number:"))
if int > 0:
    print("Positive number")
elif int < 0:
    print("Negative number")
else:
    print("Number is Zero")

a = int(input("Enter number"))
b = int(input("Enter number"))
c = int(input("Enter number"))
if a>=b and a>=c:
    print("a is greater")
elif b>=a and b>=c:
    print("b is greater")
elif a==b and a==c:
    print("All are equal")     
else:
    print("c is greater")


int = int(input("Enter year:"))
if int % 4 == 0 and int % 100 != 0 or int % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")'''


a = int(input("Enter your number:"))
b = int(input("Enter your number:"))
oporation = input("Enter operation (+, -, *, //):")
if oporation == "+":
    print(a+b)
elif oporation == "-":
    print(a-b)
elif oporation == "*":
    if b==0:
        print("0")
    else:
        print(a*b)
elif oporation == "//":
    if b==0:
        print("Division by zero is not allowed") 
    else:
        print(a//b)
else:
    print("invalid oporation")

