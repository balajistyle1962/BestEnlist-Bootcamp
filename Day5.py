print("BestEnlist Bootcamp Python 2021\n Balaji.N.R.")
list1=[1,7,15,2,7] #Declaring list
#function for adding elements in a list
def add(a): 
    list1.append(a)
    print("New list:")
    print(list1)

#function for removing a specific element from list
def delete(b):
    list1.remove(b)
    print("New list:")
    print(list1)
    
while(True):
    print("Enter a choice to add or delete an element in a list:")
    ch=int(input())
    if(ch==1):
        print("Adding an element in a list:")
        a=int(input("Enter a element to add:"))
        add(a)
    elif(ch==2):
        print("Deleting an element in the list:")
        b=int(input("Enter element to be deleted(to be present in list):"))
        delete(b)
    else:
        break

#Storing maximum and minimum element in a list
maximum=max(list1)
minimum=min(list1)
print(maximum)
print(minimum)

#creating tuple
list2=list()
n=int(input("Enter Number of elements in tuple:"))
print("Enter Elements")
for i in range(0,n):
    ele=int(input())
    list2.append(ele)
tuple1=tuple(list2)
print(tuple1)
#reverse of tuples
print("Reverse of the tuple is:")
print(tuple1[::-1])

#creating tuple into list
print(tuple1)
finallist=list(tuple1)
print("Converting tuple to list:")
print(finallist)


    


    
        
        
        
