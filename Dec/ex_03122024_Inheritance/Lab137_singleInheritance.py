class parent:
    gold= "2kg"
    def __init__(self):
        print("Default contructor- DC- Parent")

    def BHK2(self):
        print("2bhk")

class child(parent):
    def __init__(self):
        print("Default contructor- DC- Child")

    dimond ="dimond"
    def BHK3(self):
        print("3bhk")


child_obj = child()
print(child_obj.gold)
child_obj.BHK2()

parent_obj =parent()
# print(parent_obj.dimond)
