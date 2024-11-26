global_var = 12

def my_func():
    local_var =10
    print(local_var)
    print(global_var)

#print(global_var) can be defined inside/outside the function
my_func()
#print(local_var) can not define outside of the function