#Decorators => modifies the behaviour of the function without modifying the actual function

def add_extra_security(func):
    def wrapper():
        print("1. before the function is called")
        print("2. add helmet,licence, knee pads, gloves,jacket ")
        func()# called drive_scooty() function
        print("3.After driving function is called")
        print("4. Secured driving, leave all items")
    return wrapper()




@add_extra_security
def drive_scooty():
    print("A normal function!!!")
    print("I am driving the scooty")

# drive_scooty()