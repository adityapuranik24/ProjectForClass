class Students:

    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Job: ", self.job)

stu = Students('Aditya', 25, 'Python developer')

###########2#################
class staff:
    def __init__(self, role, dept):
        self.role = role
        self.dept = dept

class teacher(staff):
    def __init__(self, name, age, role, dept):
        self.name = name
        self.age = age
        self.role = role
        self.dept = dept
        super().__init__(self.role, self.dept)
        super().show_details()

    def show_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Role:", self.role)
        print("Department:", self.dept)

teacher = teacher("Aditya", 25, "Cyber", "Security")



###################3#################

