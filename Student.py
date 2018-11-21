class Student:


    def __init__ (self, name = "Empty", surname = "Empty", city = "Empty", group = 0, age = 0, marks = list()):
        self._name = self.validation(name, "alpha")
        self._surname = self.validation(surname, "alpha")
        self._city = self.validation(city, "alpha")
        self._group = self.validation(group, "group")
        self._age = self.validation(age, "age")
        self._marks = self.validation(marks, "mark")

    @property
    def name (self):
        return self._name

    @property
    def surname (self):
        return self._surname
    
    @property
    def city (self):
        return self._city
    
    @property
    def group (self):
        return self._group
    
    @property
    def age (self):
        return self._age
    
    @property
    def marks (self):
        return self._marks
    
    @name.setter
    def name (self, name):
        self._name = name
        
    @surname.setter
    def surname(self, surname):
        self._surname = surname
    
    @city.setter
    def city (self, city):
        self._city = city
        
    @group.setter
    def group (self, group):
        self._group = group
    
    @age.setter
    def age (self, age):
        self._age = age
    
    @marks.setter
    def marks (self, marks):
        self._marks = marks
    
    def __str__ (self):
        return "Name : {0}, Surname : {1}, City : {2}, Group : {3}, Age : {4}, Marks : {5}".format(self._name, self._surname, self._city, self._group, self._age, self._marks)
    
    def __repr__(self):
        return "{0} {1} {2} {3} {4} {5} ".format(self._name, self._surname, self._city, self._group, self._age, self._marks)
    
    def average_mark (self):
        result = 0
        for i in self._marks:
            result += int(i)
        return result / len(self._marks)


    def get_all(self):
        self.marks = [str(i) for i in self._marks]
        results = " ".join(self.marks)
        inf = list([self.name,self.surname, self.city,self.group, self.age, results])
        return inf
    
    def __lt__ (self, other):
        return self.average_mark() < other.average_mark() 
    
    def __eq__ (self, other):
        return (self._surname == other._surname)and(self.group == other.group)and(self.average_mark()== other.average_mark())and (self.name == other.name) and (self.age == other.age) and (self.city == other.city)

    
    def validation_alpha(self, value):
            value = value.strip()
            if not (value.isalpha()):
                i = True
                while i:
                    print("Attribute :", value, "is unsuitable!")
                    value = input("Please, input another one :")
                    value = value.strip()
                    if value.isalpha():
                        i = False
            return value
    
    def validation_age_group(self, value):
                if not(value.isdigit() and (0<int(value)<=100)):
                    i = True
                    while i:
                        print("Attribute :", value, "is unsuitable!")
                        value = input("Please, input another one :")
                        value = value.strip()
                        if value.isdigit() and (0<int(value)<=100):
                            i = False
                return value
    
    def validation_mark(self, value):
        result = list()
        value = value.split()
        if len(value) < 5:
            while len(value) !=5:
                value.append('0')
        for k in value:
            if (k.isdigit() and (0<=int(k)<=5)):
                result.append(int(k))
            else:
                i = True
                while i:
                    print("Mark :", k, "is unsuitable!")
                    k = input("Please, input another one :")
                    k = k.strip()
                    if k.isdigit() and (0<=int(k)<=5):
                        i = False
                        result.append(int(k))
        result = result [:5]
        return result

    def validation(self, value, _type):
        config = {
            "alpha": self.validation_alpha, 
            "group": self.validation_age_group,
            "age" : self.validation_age_group,
            "mark": self.validation_mark}
    
        if _type in config.keys():
            res = config[_type](value=value)
            return res
        else:
            print("Uncorrect")
