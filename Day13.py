import re
#check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
print("BestEnlist Python bootcamp 2021\nBalaji.N.R.")
def Specific_character(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

string=input("Enter a string:")
if(Specific_character(string)):
    print("The String is set of characters mentioned.")
else:
    print("Special characters are included. So it doesn't match")
print("-"*25)



#matches a word containing 'ab'

text = input('Enter the string : ')
if(re.findall('ab', text)):
    print('Match found with ab',re.findall('ab', text))
else:
    print('Match not found')
print("-"*25)


#check for a number at the end of a word/sentence.

print(" ")
print("program to check for a number at the end of a word/sentence")
def end_num(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False

print(end_num('abcdef'))
print(end_num('abcdef6'))
print("-"*25)

#search the numbers (0-9) of length between 1 to 3 in a given string
t=input('Enter the string : ')
x=[]
if(re.findall('[0-9][0-9][0-9]', t) or re.findall('[0-9][0-9]',t) or re.findall('[0-9]', t)):
    x+=([re.findall('[0-9][0-9][0-9]', t)] + [re.findall('[0-9][0-9]',t)] + [re.findall('[0-9]', t)])
    print('Contains digits of 1-3 length : ',x)
else:
    print('No 1-3 length numbers found numbers found')
print("-"*25)


#match a string that contains only uppercase letters

str=input('Enter the string : ')
if(re.findall('[A-Z]', str)):
    print('The string contains uppercase letters : ',re.findall('[A-Z]', str))
else:
    print('The string contains no upper case letters')
print("-"*25)


    
