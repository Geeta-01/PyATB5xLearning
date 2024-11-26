import time


def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print("Before  test execution")
        print("start time of TC ->",start_time)
        func()
        end_time = time.time()
        print("After UI test execution")
        print("Time taken to execution TC ->",end_time - start_time )
    return wrapper()

def log_decor(func):
    def wrapper():
        print("start the log")
        func()
        print("ending the logs..")
    return wrapper()


@time_decorator
@log_decor
def tc_1():
    print("execute TC-1")
    time.sleep(2)


@time_decorator
@log_decor
def tc_2():
    print("execute TC-2")
    time.sleep(5)

