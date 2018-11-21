import Students
from Constants import TEXT
print (TEXT)
a = Students.Students()
a.to_read(TEXT)
a.sort(lambda x : x._name)
key = True
while key == True:
    print("What do you want to do?")
    print("# 1 : Add item")
    print("# 2 : Remove item \n# 3 : Change item \n# 4 : Sort by avarege")
    print("# 5 : Sort by surname \n# 6 : Sort by group \n# 7 : Search \n# 8 : Print \n# 9 : Exit")
    choice = input("Make a choice:")
    choice = choice.strip()
    if not(choice.isdigit() and 1<=int(choice)<=9):
        i = True
        while i:
            print("\nChoice :", choice, "is unsuitable!")
            choice = input("Please, input another one :")
            choice = choice.strip()
            if choice.isdigit() and 1<=int(choice)<=9:
                choice = int(choice)
                i = False
    if int(choice) == 1:
        a.add_node()
    if int(choice) == 2:
        a.remove_node()
    if int(choice) == 3:
        print(a.change())
    if int(choice) == 4:
        a.sort(lambda x: x.average_mark())
    if int(choice) == 5:
        a.sort(lambda x: x._surname)
    if int(choice) == 6:
        a.sort(lambda x: x._group)
    if int(choice) == 7:
        to_find = input("What are you looking for : ")
        for i in a.r_search(to_find): print (a._data[i]) 
    if int(choice) == 8:
        print(a)
    if int(choice) == 9:
        key = False
