import statistics
print("BestEnlist Bootcamp python Day8")
print("Balaji.N.R")
#Sort the value from descending to ascending in list.
n=int(input("Enter number of elements in the list"))
list1=[]
for i in range(0,n):
    ele=int(input("Enter elements:"))

    list1.append(ele)
for i in range(0,n):
    for j in range(i,n):
        if(list1[i]<list1[j]):
            temp=list1[i]
            list1[i]=list1[j]
            list1[j]=temp
print("Printing sorted descending to ascending in list")
print(list1)
#converting list to set
print(set(list1))
print("*"*25)

#list number of items in a dictionary key
n=int(input("Enter number of elements in dictionary:"))
d=dict()
for i in range(n,0,-1):
    d[i]=input()
print(d)
print("Number of items in dictionary key")
print(len(d.keys()))
#sorting dictionary
for i in sorted (d.keys()):
    print(i, end = " ")
print("*"*25)

#get a string from a given string(user input)
str=input("Enter a String as input:")    
#change the first occurrence of the word to a user specified input.
ch=list()
ch=list(str)
a=input("Enter Word to be replaced in the string")
ch[0]=a
str1="".join(ch)
print(str1)
print("*"*25)

#get a string from a given string where all
strstr=input("Enter a string")
#occurrences of its first char have been changed to capital letter.
print(strstr.title())
print("*"*25)


#find the repeated items of a list
listn=[1,70,70,5,25,1,22,1,70]
repeated=list()
for i in range(0,len(listn)):
    k=i+1
    for j in range(k,len(listn)):
        if(listn[i]==listn[j] and listn[i] not in repeated):
            repeated.append(listn[i])
print("Repeated Items:")
print(repeated)
print("*"*25)

#check the sum of three elements
a=int(input("Enter 1st element:"))
b=int(input("Enter 2nd element:"))
c=int(input("Enter 3rd element:"))
sum=a+b+c
print("Enter Element in which to be deleted:")
div=int(input())
divide=sum/div
print(divide)
print("*"*25)

#Mean,median,mode among three given numbers.
a1=int(input("Enter first number:"))
b1=int(input("Enter second number:"))
c1=int(input("Enter thrid number:"))
mean=(a1+b1+c1)/3
list5=[a1,b1,c1]
list5.sort()
median=list5[1]
print("Mean:",mean)
print("Median:",median)
print("Mode:",statistics.mode(list5))
print("*"*25)



#swap cases of a given string
String=input("Enter Character:")
result=""
for i in String:
    if i.isupper():
        result+=i.lower()
    else:
        result+=i.upper()
print(result)
print("*"*25)

#convert an integer to binary & octal & decimal
n1=int(input("Enter integer:"))
print("Binary value of integer:",bin(n1))
print("Octal value of integer:",oct(n1))
print("Decimal value of integer:",n1)
print("*"*25)

    
    
    



    



    





    





    
