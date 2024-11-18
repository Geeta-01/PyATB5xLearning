browser_name = input("Enter the browser name")
match browser_name:
    case "firefox":
        print("starting firefox!!!!!!!!!")
    case "chrome":
        print("starting chrome!!!!!!!!!")
    case "internet explorer":
        print("starting IE")
    case "safari":
        print("Starting Safari!!!!!1")
    case _:
        print("browser not found!!!")