# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)

# Here are some basic argument specifiers you should know:
#
# %s - String (or any object with a string representation, like numbers)
#
# %d - Integers
#
# %f - Floating point numbers
#
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#
# %x/%X - Integers in hex representation (lowercase/uppercase)
data = ("John", "Doe", 53.44)
format_string = "Hello"

print(format_string,data[0] + " " + data[1] + ". Your current balance is %s" %data[2])

#As you can see, the first thing you learned was printing a simple sentence.
# This sentence was stored by Python as a string. However, instead of immediately printing strings out,
# we will explore the various things you can do to them.
# You can also use single quotes to assign a string.
# However, you will face problems if the value to be assigned itself contains single quotes.
# For example to assign the string in these bracket(single quotes are ' ')
# you need to use double quotes only like this

astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))
print("the index of string related character 'o' is:",astring.index("o"))
print(astring.count("l"))
print("the index of string related character 'w' is:",astring.index("w"))
print(astring[3:7])
astring = "Hello world!"
print(astring[3:7:2])
astring = "Hello world!"

print(astring[3:7])
print(astring[2:7:-1])

astring = "Hello world!"
print(astring[::-1])

astring = "Hello world!"
print(astring.upper())
print(astring.lower())

astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))