def getvalue():
    a=int(input("Enter first number:"))
    b=int(input("Enter Second number:"))
    print("Addition of two numbers is:",add(a,b))#function call
    print("Subtraction of two numbers is:",sub(a,b))
    print("Multiplication of two numbers is:",mul(a,b))
    print("Division of two numbers is:",div(a,b))
    
def add(a,b):#function definition for addition
    return a+b
def sub(a,b):#function definition for subtraction
    return a-b
def mul(a,b):#function definition for multiplication
    return a*b
def div(a,b):#function definition for division 
    return a/b

print("BestEnlist Bootcamp python 2021\nBalaji.N.R.")
getvalue()
print("*********************************************\n")

#Covid() function
def printdetails(p,t):#printing details
    print("Patient Name:",p)
    print("Patient current temperature:",t)
    
    
def covid(name,temperature=98):#covid() function
    patientname=name
    finaltemp=temperature
    printdetails(patientname,finaltemp)

covid("xxxxxx",99)
covid("xyxyxyu")
covid("yyyyy",105)
covid("aaabaa")

