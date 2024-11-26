#function within function

def say_hello():
    print("Hi all,")
    greet()

def greet():
    print(" welcome to python hub")

say_hello()
greet()
say_hello()