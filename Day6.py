print("BestEnlist Bootcamp Python 2021 Balaji.N.R.")
#Removing a key from Dictionary
a={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten"}
n=int(input("Enter key in which you want to delete:"))
if n in a:
    del a[n]
print(a)

#Write a Python program to map two lists into a dictionary
keys = [1,2,3,4,5,6]
values = ["One","Two","Three","Four","Five","Six"]
final_dict = dict(zip(keys, values))
print(final_dict)

#length of a set
set1={1,2,75,47,25,10}
set1.add(20)
set1.add(21)
print("The Length of the given set is:")
print(len(set1))

#Remove the intersection of a 2nd set from the 1st set
s1={1,2,3,45,15}
s2={45,2,50,60,70}
print("Intersection of two sets:")
print(s1.intersection(s2))
print("Removing intersection of second set from first set:")
print(s1.difference(s2))






