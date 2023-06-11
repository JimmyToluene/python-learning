#Conditionals
#Some symbols > >= < <= == !=(Not equal)
x = int(input("What's x?"))
y = int(input("What's y?"))

#Frist version conditional quote
if x < y :
    print(x,"is less than ",y)
elif x > y:
    print(x,"is larger than",y)
else:
    print(x,"is equal to ",y)

#Second version conditional quote
     #The if con1:
     #     else:

#New key word : or
if x < y or x > y:
    print("x is not euqal to y")
else:
    print("x is equals to y")

#Other substution
if x != y:
    print("x is not euqal to y")
else:
    print("x is euqal to y")
    