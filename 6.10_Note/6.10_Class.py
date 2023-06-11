#The variables,parameters,and some function's prototype.
#name = input("What is your name?\n")

name = input("What is your name?\n").strip().title()
 #Benefits:
 #Shorts:If the input is too long,the input will be too long to read clearly.
 #no right answer!
 #strip() function just remove the left and right space in this function but it will not remove the middle space.
   #For example,"  jimmy toluene  " it final output is "jimmy toluene"

 #How many .fun1().fun2() can did in python?

 #Assign operator for right hand input function return value to left variable name;

#str variable
#Some documentation of string docs.python.org/3/library/stdtypes.html#string-methods

  #1.One of example to change str in order to Remove whitespace from str.
# name = name.strip()
  #2.Capitalize user's name
  #but the capitalize doesn't means that first letter related to every words will be capitalized.Instead,it
  #just will capitalize first words.
# name = name.capitalize()

# name = name.title()
   #this function will capitalize every first letter in every words.
# name = name.strip().title()

#Split user's name into first name and last name
first,last = name.split(" ")
print(f"0.hello,{first}")

print("1.hello,",name)
#the variable named name,it is a string.
#The argument are add with a space automaticly.

print("2.hello," + name)
#second version of this print.The string is added to first string by PLUS symbol.

print("3.hello,")
print(name)
#Third way to express the print function.

print("4.hello,",end="")
print(name)

print("5.hello,",name,sep='')

#the print function's default setting.The prototype of this function "print" list at below.
#Here is a prototype of function print();
             #print(*objects,      sep=' ',       end='\n',      file=None,     flush=False)

             #Four arguments/parameters are listed above.
             #1: *object:it means that all object can be the parameter of this function
             #2: the multiple arguments related to this function will be automaticaly add a space aims to seperate them
             #3: the defalut value of this end parameters is '\n'.
#parameters
   #name parameters
   #positional parameters

# What if we want to print some quotation in python?

#Some coner case...

print('6.hello,"toluene"')
#      ^                 ^
# We can attempt some stategy to use the single quote on outside to solve the problem we met.
# Then we can get the final result {hello,"toluene"}

#Or other stragety is
print("7.hello,\"toluene\"")
#               ^        ^
#Escape characters.This characters can let computer to recongnize some special characters.

##print("hello,{name}") #wrong case!
#format string:{}
#How to use it?
print(f"8.hello,{name}")


