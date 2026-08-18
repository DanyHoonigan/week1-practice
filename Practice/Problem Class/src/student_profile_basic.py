class StudentProfile():
    def __init__(self,student_id,name,course,email,skills):
        self.Id = student_id
        self.name = name
        self.course = course
        self.email = email
        self.skills = skills
    def __str__(self):
        return(
            f"Student ID: {self.Id}\n"
            f"Student Name: {self.name}\n"
            f"Student Course: {self.course}\n"
            f"Student email: {self.email}\n"
            f"Student Skills: {', '.join(self.skills)}"
        )
n = int(input("Enter number of students: "))
for i in range(n):
    Id = int(input("Enter student ID: "))
    name = input("Enter name: ")
    course = input("Enter course: ")
    email = input("Enter your email: ")
    num = int(input("Enter number of skills:"))
    skill = []
    for i in range(num):
        o = input("Enter your skill: ")
        skill.append(o)
student = StudentProfile(Id,name,course,email,skill)
print(student)