print("BestEnlist Bootcamp Python 2021\nBalaji.N.R.\nDay14\n")
# 1.List down all the error types and check all the errors using a python program for all errors
try:
    print(s)

except NameError :
    print("Name error")
print("*"*25)
    

    
# 2. Design a simple calculator app with try and except for all use cases

print("SIMPLE CALCULATOR ")

a=int(input("Enter 1st Number "))
b=int(input("Enter 2nd number "))

c=input("Enter operation ")
if(c=='+'):
    print(a+b)
elif(c=='-'):
    print(a-b)
elif(c=='*'):
    print(a*b)
elif(c=='/'):
    try:
        z=a/b
        print(z)
    except ZeroDivisionError:
        print("zero division error")
    finally:
        print("*"*25)

      




        
# 3. print one message if the try block raises a NameError and another for other errors
print(" ")
print("print one message if the try block raises a NameError and another for other errors")
try:
    a=int(input("Enter Positive integer:"))
    if a<0:
        print(b)
        raise NameError("Name Error")
    if a==0:
        raise ValueError("Value Error")
except NameError as n:
    print(n)
except ValueError as v:
    print(v)
print("*"*25)


    
# 4. When try-except scenario is not required?
print("try catch is needed only if expected error is small and does not affect the program, in case of fatal errors try catch block is not recommended")
print("*"*25)

# 5. Try getting an input inside the try catch block
print(" ")
print("input inside the try catch block")
try:
    n=input()
    a=int(n)
    print(a)
except:
    print("Invalid input")
print("*"*25)

