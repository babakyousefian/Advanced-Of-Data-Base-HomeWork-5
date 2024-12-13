from fastapi import APIRouter
from my_lorestan_univ_list.myLorestanUnivList import *
from database.mydatabase import *
from mySchema.my_Schema import *
from bson import ObjectId

my_Router = APIRouter()

@my_Router.get("/Data/Read/")
async def read_lorestan_univ():

    students = list_serial_student(student_collection.find())
    lecturers = list_serial_lecturer(lecturer_collection.find())
    courses = list_serial_course(course_collection.find())
    course_registers = list_serial_course_register(CourseRegister_collection.find())
    presented_courses1 = list_serial_presented_courses(PresentedCourses_collection.find())
    return [
        students,
        lecturers,
        courses,
        course_registers,
        presented_courses1
    ]

@my_Router.post("/Data/Create/")
async def create_lorestan_univ(stu:student , lec:lecturer , cors:course , cr:CourseRegister , pc:PresentedCourses):

    student_collection.insert_one(dict(stu))
    lecturer_collection.insert_one(dict(lec))
    course_collection.insert_one(dict(cors))
    CourseRegister_collection.insert_one(dict(cr))
    PresentedCourses_collection.insert_one(dict(pc))


@my_Router.put("/Data/Update/{stu_id:str , lec_id:str , cors_id:str , cr_id:str , pc_id:str}")
async def update_lorestan_univ(stu_id:str , lec_id:str , cors_id:str , cr_id:str , pc_id:str , stu:student , lec:lecturer , cors:course , cr:CourseRegister , pc:PresentedCourses):

    student_collection.find_one_and_update({"_id":ObjectId(stu_id)} , {"$set":dict(stu)})
    lecturer_collection.find_one_and_update({"_id":ObjectId(lec_id)} , {"$set":dict(lec)})
    course_collection.find_one_and_update({"_id":ObjectId(cors_id)} , {"$set":dict(cors)})
    CourseRegister_collection.find_one_and_update({"_id":ObjectId(cr_id)} , {"$set":dict(cr)})
    PresentedCourses_collection.find_one_and_update({"_id":ObjectId(pc_id)} , {"$set":dict(pc)})


@my_Router.delete("/Data/Delete/{stu_id:str , lec_id:str , cors_id:str , cr_id:str , pc_id:str}")
async def delete_lorestan_univ(stu_id:str , lec_id:str , cors_id:str , cr_id:str , pc_id:str):

    student_collection.find_one_and_delete({"_id":ObjectId(stu_id)})
    lecturer_collection.find_one_and_delete({"_id":ObjectId(lec_id)})
    course_collection.find_one_and_delete({"_id":ObjectId(cors_id)})
    CourseRegister_collection.find_one_and_delete({"_id":ObjectId(cr_id)})
    PresentedCourses_collection.find_one_and_delete({"_id":ObjectId(pc_id)})


