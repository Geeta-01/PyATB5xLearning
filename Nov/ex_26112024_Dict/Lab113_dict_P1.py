student_info1 = {"name" : "Amit",
                "age" : 32,
                "address": {"Home address" :"KA",
                            "Office address":"NY"} }

student_info2 = {"name" : "Geeta",
                "age" : 33,
                "address": {"Home address" :"KA",
                            "Office address":"ND"} }

student_info3 = {"name" : "Vihu",
                "age" : 12,
                "address": {"Home address" :"Goa",
                            "Office address":"Vizag"} }
student_list = [student_info1,student_info2, student_info3]
print(student_list)
print(student_list[0])
print(student_list[1])
print(student_list[0]["name"])
print(student_list[0]["address"])
print(student_list[0]["address"]["Office address"])

print(student_list[2]["address"]["Office address"])




