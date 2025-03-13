students = [
    {'firstname':'John', 'lastname':'Smith','Age':17}, 
    {'firstname':'Harry', 'lastname':'Styles','Age':16}, 
    {'firstname':'Cody', 'lastname':'Mills','Age':18}
]

students_list = []

for i in students:
    ls = [i["firstname"], i["lastname"], i["Age"]]
    students_list.append(ls)

for i in students_list:
    print(i)

