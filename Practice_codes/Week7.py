# class student:
#     def __int__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def details(self):
#         print("Aditya Puranik")
#
# d = student("aditya", 25)

class person:
    counter = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        person.counter += 1
#
    def greet(self):
        return f"Hi, it's {self.name}."
#
# p1 = person('John', 25)
# # p2 = person("Jane", 25)
# # print(person.counter)

# @classmethod
# def create_anonymous(cls):
#     return person("anonymous", 22)

#
# anonymous = person.create_anonymous()
# print(anonymous.name)

class employee(person):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title

    def greet(self):
        return super().greet() + f"I'm a {self.job_title}"

em = employee('john', 25, 'Python developer')













