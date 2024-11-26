
def add_before_and_after_UI_tc(func):
    def wrapper():
        print("Before UI test execution")
        print("start the browser")
        func()
        print("After UI test execution")
        print("close the browser")
    return wrapper()


@add_before_and_after_UI_tc
def test_UI_tc():
    print("I will test the UI Test cases")
    # tc_1()
    # tc_2()

@add_before_and_after_UI_tc
def tc_1():
    print("execute TC-1")
@add_before_and_after_UI_tc
def tc_2():
    print("execute TC-2")