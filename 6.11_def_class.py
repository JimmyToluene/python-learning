#How to define a funtion?
def hello():
    name = input("What is your name?\n").strip().title()
    print(f"hello,{name}")

def hello_2(to="world"):
    print("hello,"+ to)

hello_2()

