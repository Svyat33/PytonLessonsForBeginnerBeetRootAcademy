'''Task 1
School
Make a class structure in python representing people at school. Make a base class called Person, a class called Student,
and another one called Teacher. Try to find as many methods and attributes as you can which belong to different classes,
and keep in mind which are common and which are not. For example, the name should be a Person attribute,
while salary should only be available to the teacher. '''
'''Школа Создайте структуру классов в Python, представляющую людей в школе. Создайте базовый класс с именем Person,
 класс с именем Student и еще один с именем Teacher. Постарайтесь найти как можно больше методов и атрибутов,
  которые принадлежат разным классам, и имейте в виду, какие распространены, а какие нет. Например,
   имя должно быть атрибутом Person, а зарплата должна быть доступна только учителю.'''


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
     
    def printname(self):
        print(self)
      
    def __str__(self):
        return f"{self.fname} {self.lname}"
      
class Student(Person):
    def __init__(self, fname, lname, group, course, faculty, form_of_education):
        super().__init__(fname, lname)
        self.group = group
        self.course = course
        self.faculty = faculty
        self.form_of_education = form_of_education
        
    def printstudent(self):
        print(self.group, self.course, self.faculty, self.form_of_education)
      
      
class Teacher(Person):
    def __init__(self, fname, lname, object_of_study, salary):
        super().__init__(fname, lname)
        self.object_of_study = object_of_study
        self.salary = salary
      
    def printteacher(self):
        print(self.object_of_study, self.salary)
      
      
if __name__ == "__main__":
    student1 = Student("Revenko", "Vitalii", "201", "2", "IT", "budget")
    print(f"ФИО студента:\t{student1}")
    student1.printname()
    student1.printstudent()
    print("-=-" * 10)
    teacher = Teacher("Shevchenko", "Taras", "Literatura", "1000")
    teacher.printname()
    teacher.printteacher()
    print(f"Учитель: {teacher}")
