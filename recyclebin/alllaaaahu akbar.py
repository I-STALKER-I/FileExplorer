# defining list to store students, professors and calasses objects
students = []
professors = []
kelasha = []


class student:
    # define a list to store student ids
    student_ids = []
    def __init__(self, name, student_id, entering_year, field):
        if student_id in (student.student_ids + professor.professor_ids):
            print("this identical number previously registered")
        else:
            self.name = name
            self.id = student_id
            self.entering = entering_year
            self.field = field
            self.classes = {}
            student.student_ids.append(student_id)
            students.append(self)
            print("welcome to golestan")
    # defining add_student request
    def add_student(std_id, class_id):
        if std_id not in student.student_ids:
            print("invalid student")
            
        elif class_id not in classes.class_ids:
            print("invalid class")
        else: 
            case_student = next(x for x in students if x.id == std_id)
            case_class = next(x for x in kelasha if x.id == class_id)
            if case_student.field != case_class.field:
                print("student field is not match")
            elif class_id in list(case_student.classes.keys()):
                print("student is already registered")
            else:
                case_student.classes.update({class_id:None})
                case_class.std.append(std_id)
                case_class.grades.update({std_id:None})
                print("student added successfully to the class")

    # defining student_status request
    def student_status(std_id):
        if std_id not in student.student_ids:
            print("invalid student")
        else:
            case_student = next(x for x in students if x.id == std_id)
            case_student_classes = list(case_student.classes.keys())
            try:
                print(case_student.name, case_student.entering, case_student.field, *(next(case for case in kelasha if case.id == item).name for item in case_student_classes), sep = " ")
            except:
                print(case_student.name, case_student.entering, case_student.field, sep = " ")

    # defining set_final_mark request
    def set_final_mark(prof_id, std_id, cls_id, mark):
        if prof_id not in professor.professor_ids:
            print("invalid professor")

        elif std_id not in student.student_ids:
            print("invalid student")
            
        elif cls_id not in classes.class_ids:
            print("invalid class")
        
        else:
            case_class = next(item for item in kelasha if item.id == cls_id)
            case_student  = next(item for item in students if item.id == std_id)
            if case_class.professor != prof_id:
                print("professor class is not match")
            elif std_id not in case_class.std:
                print("student did not registered")
            else:
                case_student.classes.update({case_class.id:int(mark)})
                case_class.grades.update({case_student.id:int(mark)})
                print("student final mark added or changed")
    # defining mark_studnet request
    def mark_student(std_id, cls_id):
        if std_id not in student.student_ids:
            print("invalid student")
            
        elif cls_id not in classes.class_ids:
            print("invalid class")
        else:
            case_class = next(item for item in kelasha if item.id == cls_id)
            case_student = next(item for item in students if item.id == std_id)
            if std_id not in case_class.std:
                print("student did not registered")
            else:
                print(case_student.classes[cls_id])
    # defining average_mark_student request
    def average_mark_student(std_id):
        if std_id not in student.student_ids:
            print("invalid student")
        else:
            case_student = next(item for item in students if item.id == std_id).classes.values()
            non_grades = []
            for grades in list(case_student):
                if grades != None:
                    non_grades.append(grades)
            grade_sum = sum(non_grades)
            grade_number = len(non_grades)
            if grade_number == 0:
                print("None")
            else:
                print("%.2f" %(grade_sum/grade_number))
    # top_student request
    def top_student(field, entering_year):
        max_number = -1
        case = "None"
        flag = True
        for item in students:
            if item.field == field and item.entering == entering_year:
                flag = False
                case_grades = item.classes.values()
                non_grades = []
                for grades in list(case_grades):
                    if grades != None:
                        non_grades.append(grades)
                grade_sum = sum(non_grades)
                grade_number = len(non_grades)
                if grade_number != 0 and (grade_sum/grade_number) > max_number:
                    max_number = (grade_sum/grade_number)
                    case = item.name
        # check if there is a student with such conditions
        if flag:
            print("None")
        else:
            print(case)
            flag = True
            case = None


        

class professor:
    # define a list to store professor ids
    professor_ids = []
    def __init__(self, name, professor_id, field):
        if professor_id in (student.student_ids + professor.professor_ids):
            print("this identical number previously registered")
        else:
            self.name = name
            self.id = professor_id
            self.field = field
            self.classes = []
            professor.professor_ids.append(professor_id)
            professors.append(self)
            print("welcome to golestan")
    # add_professor request
    def add_professor(prof_id, class_id):
        if prof_id not in professor.professor_ids:
            print("invalid professor")
            
        elif class_id not in classes.class_ids:
            print("invalid class")
        else:
            case_professor = next(x for x in professors if x.id == prof_id)
            case_class = next(x for x in kelasha if x.id == class_id)
            if case_professor.field != case_class.field:
                print("professor field is not match")
            elif case_class.professor != None:
                print("this class has a professor")
            else:
                case_class.professor = prof_id
                case_professor.classes.append(class_id)
                print("professor added successfully to the class")

    # professor_status request
    def professor_status(prof_id):
        if prof_id not in professor.professor_ids:
            print("invalid professor")
        else:
            case_professor = next(x for x in professors if x.id == prof_id)
            case_professor_classes = case_professor.classes
            try:
                print(case_professor.name, case_professor.field, *(next(case for case in kelasha if case.id == item).name for item in case_professor_classes), sep = " ")
            except:
                print(case_professor.name, case_professor.field, sep = " ")

    # average_mark_professor request
    def average_mark_professor(prof_id):
        if prof_id not in professor.professor_ids:
            print("invalid professor")
        else:
            flag = False
            grade_sum = 0
            grade_numbers = 0
            case_classes = next(item for item in professors if item.id == prof_id).classes
            if case_classes == []:
                flag = True
            else:
                for cls_id in case_classes:
                    grades = next(item for item in kelasha if item.id == cls_id).grades.values()
                    non_grades = []
                    for item in list(grades):
                        if item != None:
                            non_grades.append(item)
                    grade_sum += sum(non_grades)
                    grade_numbers += len(non_grades)
            if grade_numbers == 0 or flag == True:
                print("None")
            else:
                print("%.2f" %(grade_sum/grade_numbers))


class classes:
    # define a list to store class ids
    class_ids = []
    def __init__(self, name, class_id, field):
        if class_id in classes.class_ids:
            print("this class id previously used")
        else:
            self.name = name
            self.id = class_id
            self.field = field
            self.professor = None
            self.std = []
            self.grades = {}
            classes.class_ids.append(class_id)
            kelasha.append(self)
            print("class added successfully")

    # class_status request
    def class_status(cls_id):
        if cls_id not in classes.class_ids:
            print("invalid class")
        else:
            case_class = next(x for x in kelasha if x.id == cls_id)
            # check if the class has any professor
            if case_class.professor == None:
                prof = "None"
            else:
                prof = next(case for case in professors if case.id == case_class.professor).name
            try:
                print(prof, *(next(case for case in students if case.id == item).name for item in case_class.std), sep = " ")
            except:
                print(prof)

    # mark_list request
    def mark_list(cls_id):
        if cls_id not in classes.class_ids:
            print("invalid class")
            return
        case_class = next(item for item in kelasha if item.id == cls_id)
        if case_class.professor == None:
            print("no professor")
        elif case_class.std == []:
            print("no student")
        else:
            print(*(case_class.grades.values()), sep = " ")

    # top_mark request
    def top_mark(cls_id):
        if cls_id not in classes.class_ids:
            print("invalid class")
        else:
            case_class = next(item for item in kelasha if item.id == cls_id).grades.values()
            non_grades = []
            for item in list(case_class):
                if item != None:
                    non_grades.append(item)
            if non_grades == []:
                print("None")
            else:
                print(max(non_grades))

# reading and storing inputs in a list
reading = []
while True:
    case = input()
    if case == "end":
        break
    reading.append(case.split())

for case in reading:
    # implementing first part
    # register student request
    if case[0] == "register_student":
        student(case[1], case[2], case[3], case[4])

    # register professor request
    elif case[0] == "register_professor":
        professor(case[1], case[2], case[3])

    # make_class request
    elif case[0] == "make_class":
        classes(case[1], case[2], case[3])

    # add_studnet request
    elif case[0] == "add_student":
        student.add_student(case[1], case[2])

    # add_professor request
    elif case[0] == "add_professor":
        professor.add_professor(case[1], case[2])

    # studnet_status request
    elif case[0] == "student_status":
        student.student_status(case[1])

    # professor_status request
    elif case[0] == "professor_status":
        professor.professor_status(case[1])
    
    # class_status request
    elif case[0] == "class_status":
        classes.class_status(case[1])

    # set_final_mark request
    elif case[0] == "set_final_mark":
        student.set_final_mark(case[1], case[2], case[3], case[4])
    
    # mark_student request
    elif case[0] == "mark_student":
        student.mark_student(case[1], case[2])

    # mark_list request
    elif case[0] == "mark_list":
        classes.mark_list(case[1])

    # average_mark_professor request
    elif case[0] == "average_mark_professor":
        professor.average_mark_professor(case[1])

    # average_mark_student request
    elif case[0] == "average_mark_student":
        student.average_mark_student(case[1])
    
    # top_student request
    elif case[0] == "top_student":
        student.top_student(case[1], case[2])
    
    # top_mark request
    elif case[0] == "top_mark":
        classes.top_mark(case[1])