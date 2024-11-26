#Function with default argument with no return
def greet_by_name(name="Geeta"):
    print(name.upper())

greet_by_name()
greet_by_name("Vihaan")

def mul_args(name1="A", name2 = "B"):
    print("Multiple Arguments->", name1, name2)

mul_args()
mul_args("geeta")
mul_args("geeta", "g")
mul_args("g")
mul_args(name2= "Vihaan")