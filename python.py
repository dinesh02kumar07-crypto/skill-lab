'''import getpass
import keyword
import os
print(keyword.kwlist)
a=None
print(a)
a=0
print(type(a))
print(bool(a))
import keyword
print (keyword.kwlist)


a=None
print(a)
a=0
print(type(a))
print(bool(a))
print(bool(0.0))
print(bool(1.8))
print(int())
a=3j+5
print(a)
a="happy father's day"
print(a)

#to access f
print(a[6])
"list"
my_list=[1,2,3,4,'hello',5.6, 'true']

#to extract hello from the list
print(my_list[4])
#now H from hello

print(my_list[4][0])
#append function

my_list.append(10)
print(my_list)
#pop function

print(my_list.pop())
print(my_list)

#finding data type of list
print(type(my_list))

#tuple
my_tuple=(1,2,3,'hello',5.6,'true')

#set operstions 
set1={1,2,3,'hello',5.6,'true'}
print(type(set1))
my_dict={'a':[10,20,30],'b':[40]}
print(my_dict['a'][-2])

#list of keys
print(my_dict.keys())

"slicing"
a="hello world"
print(a[0:5])
print(a[6:11])
print(a[2:4])
print(a[2:3+1:3])

#accesing from right to left
print(a[-8:-10:-1])
a="Good Morning"
print(a[7:11])

#Same with negative indexing 
print(a[-5:-1])
a="Hello"
print(a[-2:-5:-1])
print(a[::-1]) #Reverse the string
a="Good Morning"

# extract oodM
print(a[1:5+1:2])

#extract Mng
print(a[5::3])
print(a[-7::3])
print(a[3:0:-1])
print(a[10:4-1:-3])

#collection of type input
a = eval(input("Enter : "))
print(a,type(a))
b = int(input("enter:"))
if b % 2==0:
    print("Even")
else:
    print("odd")
c = input("Enter:")
if len(c) == 5:
    print("the length of the list of 5")
else:
    print("the length of the list is not 5")

print(ord('j')+ord('a')+ord('v')+ord('a'))
print(chr(65))
print(chr(95))
#how to change capital latter to small letter without using inbuilt function
chr = input("Enter a capital letter : ")
if "A" < chr < "Z":
    print("upper case letter")
elif "a" < chr < "z":
    print("lower case letter")
else:
    print("not a letter")
un = input("Enter a user name : ")
if un =='hero':
    password = getpass.getpass("Enter a password : ")
    expected_password = os.environ.get("HERO_PASSWORD")
    if expected_password is None:
        print("Set the HERO_PASSWORD environment variable.")
    elif password == expected_password:
        print("successfully logged in")
    else:
        print("incorrect password")        
else:
    print("incorrect user name")

i=1
while i<=100:
    print(i)
    i+=1
n= int(input("Enter a number : "))
rev=0
while(n <0):
    ld=n%10
    n= n//10
    rev=rev*10+ld
print(rev)'''
'''#Nested for Loops 
for i in range(1, 6):
    for j in range(1, 6):
        print('*', end=' ')
    print()'''



'''for i in range(1, 6):
    for j in range(1, 6):
        if i==j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''
'''a-"happy birthday"
pritn(a[-4:-7:-1])'''

'''#Functions
#With Args and return 
def convert(s,out):
    out=""
    for i in s:
        if "A"<=i<="Z":
            out+=chr(ord(i)+32)
        elif "a"<=i<="z":
            out+=chr(ord(i)-32)
        else:
            out+=i
    return out         #Address of the output string is returned to the calling function not value

print(convert(input("Enter a string: "),'' ))'''


'''#With Args and no return 

def convert_no_return(s, out):
    out=""
    for i in s:
        if "A"<=i<="Z":
            out+=chr(ord(i)+32)
        elif "a"<=i<="z":
            out+=chr(ord(i)-32)
        else:
            out+=i
    print(out)
convert_no_return(input("Enter a string: "),'' )'''
'''#Without Args and with return
def convert_no_args():
    s=input("Enter a string: ")
    out=""
    for i in s:
        if "A"<=i<="Z":
            out+=chr(ord(i)+32)
        elif "a"<=i<="z":
            out+=chr(ord(i)-32)
        else:
            out+=i
    return out
print(convert_no_args())'''

'''#Without Args and no return
def convert_no_args_no_return():
    s=input("Enter a string: ")
    out=""
    for i in s:
        if "A"<=i<="Z":
            out+=chr(ord(i)+32)
        elif "a"<=i<="z":
            out+=chr(ord(i)-32)
        else:
            out+=i
    print(out)
convert_no_args_no_return()'''


class college:
    cname="GPLN"
    cloc="Hoodi"
s1=college()
'''print(s1.cname,s1.cloc)
college.cloc="Bangalore"
print(college.cloc)
print(s1.cloc)'''
print("Changing location wrt object")
s1.cloc="Mysore"
print(s1.cloc)
print(college.cloc)
