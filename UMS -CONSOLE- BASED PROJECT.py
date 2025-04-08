class Person:
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name

class Student(Person):
    def __init__(self, rollno, name, branch):
        super().__init__(rollno, name)
        self.branch = branch

class Teacher(Person):
    def __init__(self, rollno, name, subject):
        super().__init__(rollno, name)
        self.subject = subject

class College:
    def __init__(self, cname):
        self.cname = cname
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def display_students(self):
        if not self.students:
            print("No students found.")
            return
        for i, student in enumerate(self.students, 1):
            print(f"\nStudent {i}:")
            print(f"Roll Number: {student.rollno}")
            print(f"Name       : {student.name}")
            print(f"Branch     : {student.branch}")

    def display_teachers(self):
        if not self.teachers:
            print("No teachers found.")
            return
        for i, teacher in enumerate(self.teachers, 1):
            print(f"\nTeacher {i}:")
            print(f"Roll Number: {teacher.rollno}")
            print(f"Name       : {teacher.name}")
            print(f"Subject    : {teacher.subject}")

    def search_student_by_rollno(self, rollno):
        for student in self.students:
            if student.rollno == rollno:
                return student
        return None

    def search_teacher_by_rollno(self, rollno):
        for teacher in self.teachers:
            if teacher.rollno == rollno:
                return teacher
        return None


colleges = []

while True:
    print("\nChoose the Required option: ")
    print("1. Create College.")
    print("2. Add Student.")
    print("3. Add Teacher.")
    print("4. Display Students.")
    print("5. Display Teachers.")
    print("6. Search Student by Roll Number.")
    print("7. Search Teacher by Roll Number.")
    print("8. Exit.")

    try:
        choice = int(input("Enter your Option: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice == 1:
        clgname = input("Enter College Name: ")
        exists = False
        for clg in colleges:
            if clg.cname == clgname:
                exists = True
                break
        if exists:
            print("\nCollege Already Exists!")
        else:
            clg = College(clgname)
            colleges.append(clg)
            print("\nCollege Added Successfully!")

    elif choice == 2:
        clgname = input("Enter College Name: ")
        clg = next((c for c in colleges if c.cname == clgname), None)
        if clg:
            rollno = input("Enter Roll Number: ")
            name = input("Enter Student Name: ")
            branch = input("Enter Branch: ")
            s = Student(rollno, name, branch)
            clg.add_student(s)
            print("\nStudent Added Successfully!")
        else:
            print("\nCollege Does Not Exist!")

    elif choice == 3:
        clgname = input("Enter College Name: ")
        clg = next((c for c in colleges if c.cname == clgname), None)
        if clg:
            rollno = input("Enter Roll Number: ")
            name = input("Enter Teacher Name: ")
            subject = input("Enter Subject: ")
            t = Teacher(rollno, name, subject)
            clg.add_teacher(t)
            print("\nTeacher Added Successfully!")
        else:
            print("\nCollege Does Not Exist!")

    elif choice == 4:
        clgname = input("Enter College Name: ")
        clg = next((c for c in colleges if c.cname == clgname), None)
        if clg:
            clg.display_students()
        else:
            print("\nCollege Does Not Exist!")

    elif choice == 5:
        clgname = input("Enter College Name: ")
        clg = next((c for c in colleges if c.cname == clgname), None)
        if clg:
            clg.display_teachers()
        else:
            print("\nCollege Does Not Exist!")

    elif choice == 6:
        clgname = input("Enter College Name: ")
        clg = next((c for c in colleges if c.cname == clgname), None)
        if clg:
            rollno = input("Enter Student Roll Number to Search: ")
            student = clg.search_student_by_rollno(rollno)
            if student:
                print("\nStudent Found:")
                print(f"Roll Number: {student.rollno}")
                print(f"Name       : {student.name}")
                print(f"Branch     : {student.branch}")
            else:
                print("\nStudent Not Found!")
        else:
            print("\nCollege Does Not Exist!")

    elif choice == 7:
        clgname = input("Enter College Name: ")
        clg = next((c for c in colleges if c.cname == clgname), None)
        if clg:
            rollno = input("Enter Teacher Roll Number to Search: ")
            teacher = clg.search_teacher_by_rollno(rollno)
            if teacher:
                print("\nTeacher Found:")
                print(f"Roll Number: {teacher.rollno}")
                print(f"Name       : {teacher.name}")
                print(f"Subject    : {teacher.subject}")
            else:
                print("\nTeacher Not Found!")
        else:
            print("\nCollege Does Not Exist!")

    elif choice == 8:
        print("\nExiting Program. Goodbye!")
        break

    else:
        print("\nInvalid Option. Please choose a valid option.")
