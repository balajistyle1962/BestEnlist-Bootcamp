import math
print("BestEnlist Bootcamp Python 2021 Day9")
print("Balaji.N.R.")
#loop through a list of numbers and add +2 to every value to elements in list
n=int(input("Enter number of elements in the list:"))
list1=[]
for i in range(0,n):
    ele=int(input("Enter elements:"))
    list1.append(ele)
for i in range(0,n):
    list1[i]+=2
print(list1)
print("*"*25)

#Printing pattern
print("Printing Desired Pattern:")
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("\n")
print("*"*25)


#Print the Fibonacci sequence
n=int(input("Enter Number of series:"))
a=0
b=1
fib=0
print("Fibonacci Series is:")
for i in range(0,n+1):
    fib+=a
    a=b
    b=fib
    print(fib)
print("*"*25)

#Armstrong number
#Armstrong number is an integer such that the sum of cubes of its digits is equal to the number itself.
n=int(input("Enter an integer:"))
temp=n
sum=0
while(temp>0):
    b=temp%10
    sum+=b**3
    temp//=10
if(sum==n):#Checking whether the given integer is armstrong or not.
    print("The given number is an Armstrong number")
else:
    print("No it is not an armstrong number")
print("*"*25)

#print the multiplication table of 9
print("Multiplication tables of 9:")
for i in range(1,11):
    print("9 X %d = %d"%(i,9*i))
print("*"*25)

#program to check number is negative or positive
n=int(input("Enter a integer:"))
if(n>0):
    print("The Given number is positive")
elif(n<0):
    print("The Given number is negative")
else:
    print("The Given number is zero")
print("*"*25)

#convert the number of days to ages
days=int(input("Enter Number of days:"))
final_age=days//365
print("Age is",final_age)
print("*"*25)


#Trigonometry problem using math function
print(math.degrees(math.pi/4))
print(math.radians(60))
print("Sine function:",math.sin(math.pi/4))#sine
print("Cosine function:",math.cos(math.pi/3))#cosine
print("Tangent function:",math.tan(math.pi/2))#tangent
print("Inverse of sine in radians:",math.asin(1))
print("Inverse of cosine in radians:",math.acos(0))
print("Inverse of Tangent in radians:",math.atan(1))
print("*"*25)

#calculator using if statement
while True:
    ch=input("Enter Your Choice:")
    if ch in ('+','-','*','/'):
        num1=int(input("Enter first number:"))
        num2=int(input("Enter Second number:"))
        if(ch=='+'):
            print(num1,"+",num2,'=',num1+num2)
        elif(ch=='-'):
            print(num1,"-",num2,"=",num1-num2)
        elif(ch=='*'):
            print(num1,"*",num2,"=",num1*num2)
        else:
            print(num1,"/",num2,"=",num1/num2)
        
    else:
        print("Invalid input")
        print("*"*25)
        break

        





    
    
    
