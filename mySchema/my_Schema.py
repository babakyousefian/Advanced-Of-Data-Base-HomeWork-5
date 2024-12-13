
def my_student_serializer(student) -> dict:
    return {
        "STID" : str(student["_id"]),
        "FName" : student["FName"],
        "LName" : student["LName"],
        "Father" : student["Father"],
        "Birth" : student["Birth"],
        "IDS" : student["IDS"],
        "BornCity" : student["BornCity"],
        "Address" : student["Address"],
        "PostalCode" : student["PostalCode"],
        "CPhone" : student["CPhone"],
        "HPhone" : student["HPhone"],
        "Department" : student["Department"],
        "Major" : student["Major"],
        "Married" : student["Married"],
        "ID" : student["ID"]
    }

def list_serial_student(students) -> list:
    return [my_student_serializer(student) for student in students]

def my_lecturer_serializer(lecturer) -> dict:
    return {
        "LID" : str(lecturer["_id"]),
        "FName" : lecturer["FName"],
        "LName" : lecturer["LName"],
        "ID" : lecturer["ID"],
        "Department" : lecturer["Department"],
        "Major" : lecturer["Major"],
        "Birth" : lecturer["Birth"],
        "BornCity" : lecturer["BornCity"],
        "Address" : lecturer["Address"],
        "PostalCode" : lecturer["PostalCode"],
        "CPhone" : lecturer["CPhone"],
        "HPhone" : lecturer["HPhone"]
    }

def list_serial_lecturer(lecturers) -> list:
    return [my_lecturer_serializer(lecturer) for lecturer in lecturers]



def my_course_serializer(course) -> dict:
    return {
        "CID" : str(course["_id"]),
        "CName" : course["CName"],
        "Department" : course["Department"],
        "Credit" : course["Credit"]
    }

def list_serial_course(courses) -> list:
    return [my_course_serializer(course) for course in courses]


def my_course_register_serializer(course_register) -> dict:
    return {
        "CID": str(course_register["_id"]),
        "CName": course_register["CName"],
        "Department": course_register["Department"],
        "Credit": course_register["Credit"],
        "STID": str(course_register["_id"]),
        "FName": course_register["FName"],
        "LName": course_register["LName"]
    }


def list_serial_course_register(course_registers) -> list:
    return [my_course_register_serializer(course_register) for course_register in course_registers]


def my_presented_courses_serializer(presented_courses) -> dict:
    return {
        "CID": str(presented_courses["_id"]),
        "CName": presented_courses["CName"],
        "Department": presented_courses["Department"],
        "Credit": presented_courses["Credit"],
        "LID": str(presented_courses["_id"]),
        "FName": presented_courses["FName"],
        "LName": presented_courses["LName"]
    }

def list_serial_presented_courses(presented_courses1) -> list:
    return [my_presented_courses_serializer(presented_courses) for presented_courses in presented_courses1]
