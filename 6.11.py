# int
# A number
# The symbol related to inteager
# python support the interactive mode.
  #Type "help", "copyright", "credits" or "license" for more information.
  #>>>
#calculator 6.11

#x = 1
#x = int(input("What is x?")) #some problem will occure,if user type a non-inteager variable
#y = 2
#y = int(input("What is y?"))

#By add typeconversion of x and y,then we get final outcome with inteager.
#print(z)
#print(x + y)
#But the keyboard will see this two variable as string.The final outcome will be xy;
#z = int(x) +int(y)

#print(int(input("What is x?"))+int((input("What is y?"))))
#this is a complex long synatx.

#Float point value.
x = float(input("What is x?"))
y = float(input("What is y?"))

# round(number, ndigits=None);We
#               ^ This syntax means some thing is optional,Number of digiter you want to specify.
z = round(x + y)
print(f"The x + y input's is {z:,}")
#This operation can help this function to add some comma.

h = round(x / y,5)
print("The x/y output's is ",h,sep="")

print(f"The x/y output's is {x/y:.5f}")#This way also a good way to solve the problem by using (f"xxxx{var:.xf}")

#How to define a calcultor function
def main():
    x = int(input("What's x?"))
    print("x squared is",square(x))

def square(n):
    return n*n

main()
