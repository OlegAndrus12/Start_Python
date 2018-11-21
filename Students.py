import csv
import Student
import copy
from Constants import TEXT

class Students:
    
    def __init__(self, data = list()):
        self._data = data
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self):
        return self._data
    
    def to_read(self, TEXT):
        data = list()
        with open (TEXT, "r") as file:
            csv_reader = csv.reader(file)
            for line in csv_reader:
                a = Student.Student(*line)
                if not (a in data):
                    data.append(a)
        file.close()
        self._data = data
    
    def to_write(self, TEXT):
        with open(TEXT, "w", newline="")as file:
            csw_writer = csv.writer(file, delimiter = ",")
            for i in range(len(self.data)):
                csw_writer.writerow(self.data[i].get_all())
    
    def __str__ (self):
        s = ""
        for i in self._data:
            print(i)         
        return s
    
    def __repr__(self):
        s = ""
        for i in self._data:
            print(i)         
        return s

    def __len__(self):
        return len(self._data)


    def sort(self, key = lambda x: x.name):
        n = len(self._data)
        for i in range(n-1):
            for j in range(n-i-1):
                if str(key(self._data[j])).lower() > str(key(self._data[j+1])).lower():
                    self._data [j], self._data[j+1] = self._data[j+1], self._data[j]
        return self._data

    def add_node(self):
        name = input("Input name : ")
        surname = input("Input surname : ")
        city = input("Input city : ")
        group = input("Input group : ")
        age = input("Input age : ")
        marks = input("Input marks by space : ")
        student = Student.Student(name, surname, city, group, age, marks)
        self._data.append(student)
        self.to_write(TEXT)
        return student
    
    def r_search(self, value):
        value = value.lower()
        value = value.strip()
        result = list()
        j = -1
        for i in self.data:
            j+=1
            if value in i.name.lower():
                result.append(j)
                continue
            if value in i.surname.lower():
                result.append(j)
                continue
            if value in i.city.lower():
                result.append(j)
                continue
            if value in str(i.group):
                result.append(j)
                continue
            if value in str(i.age):
                result.append(j)
                continue
            if value.isdigit():
                if int(value) in i.marks:
                    result.append(j)
                    continue
        return result

    def remove_node(self):
        to_find = input("What are you looking for : ")
        del_index = self.r_search(to_find)
        for i in del_index:
            print("#", i, self.data[i])
        if(len(del_index) != 0):
            d = input("Choose an id of element you want to delete: ")
            if int (d) in del_index:
                a = self.data[int(d)]
                self.data.pop(int(d))
                self.to_write(TEXT)
        return a
    
    def change(self):
        to_find = input("What are you looking for : ")
        to_find = to_find.strip()
        change_index = self.r_search(to_find)
        for i in change_index:
            print("#", i, self.data[i])
        if(len(change_index) != 0):
            d = input("Choose an id of element you want to change: ")
            d = d.strip()
            if not(d.isdigit() and int(d) in change_index):
                i = True
                while i:
                    print("\nChoice :", d, "is unsuitable!")
                    d = input("Please, input another one :")
                    d = d.strip()
                    if d.isdigit() and int(d) in change_index:
                        d = int(d)
                        i = False
            d = int(d)
            past = copy.deepcopy(self.data[d])
            pas = True
            while pas == True:
                print("What do you want to change?")
                print("# 1 : Name \n# 2 : Surname \n# 3 : City \n")
                print("# 4 : Group \n# 5 : Age \n# 6 : Marks \n# 7 : Nothing")
                k = input("Make a choice : ")
                k = k.strip()
                if not(k.isdigit() and 1<=int(k)<=7):
                    i = True
                    while i:
                        print("\nChoice :", k, "is unsuitable!")
                        k = input("Please, input another one :")
                        k = k.strip()
                        if k.isdigit() and 1<=int(k)<=7:
                            k = int(k)
                            i = False
                if int(k) == 1:
                    name = input("Input new name : ")
                    self._data[d]._name = self._data[d].validation(name, "alpha")
                if int(k) == 2:
                    surname = input("Input new surname : ")
                    self._data[d]._surname = self._data[d].validation(surname, "alpha")
                if int(k) == 3:
                    city = input("Input new city : ")
                    self._data[d]._city = self._data[d].validation(city, "alpha")
                if int(k) == 4:
                    group = input("Input new group : ")
                    self._data[d]._group = self._data[d].validation(group, "group")
                if int(k) == 5:
                    age = input("Input new age : ")
                    self._data[d]._age = self._data[d].validation(age, "age")
                if int(k) == 6:
                    marks = input("Input new marks : ")
                    self._data[d]._marks = self._data[d].validation(marks, "mark")
                if int(k) == 7:
                    pas = False
                self.to_write(TEXT)  
        return past
