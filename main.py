from fastapi import FastAPI , Depends , HTTPException
import models.myModels
from database.myDatabase import engine , sessionLocal
from pydantic import BaseModel , Field
from uuid import UUID
from sqlalchemy.orm import Session
from datetime import datetime


app = FastAPI()


models.myModels.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = sessionLocal()
        yield db
    finally:
        db.close()


class Student(BaseModel):

    # STID = UUID
    FName : str = Field(min_length=1 , max_length=10)
    LName :str = Field(min_length=1 , max_length=10)
    Father : str = Field(min_length=1 , max_length=10)
    Birth : datetime
    IDS : str = Field(min_length=1 , max_length=9)
    BornCity : str = Field(min_length=1 , max_length=50)
    Address : str = Field(min_length=1 , max_length=100)
    PostalCode: int = Field(ge=10000, le=999999)
    CPhone : str = Field(min_length=11 , max_length=11)
    HPhone : str = Field(min_length=11 , max_length=11)
    Department : str = Field(min_length=1 , max_length=100)
    Major : str = Field(min_length=1 , max_length=50)
    Married : bool
    ID : str = Field(min_length=1 , max_length=11)


class lecturer(BaseModel):

    # LID : UUID
    FName: str = Field(min_length=1, max_length=10)
    LName: str = Field(min_length=1, max_length=10)
    ID : str = Field(min_length=1, max_length=11)
    Department: str = Field(min_length=1, max_length=100)
    Major : str = Field(min_length=1, max_length=50)
    Birth: datetime
    BornCity: str = Field(min_length=1, max_length=50)
    Address: str = Field(min_length=1, max_length=100)
    PostalCode: int = Field(ge=10000, le=999999)
    CPhone: str = Field(min_length=11, max_length=11)
    HPhone: str = Field(min_length=11, max_length=11)


class course(BaseModel):

    # CID = UUID
    CName : str = Field(min_length=1 , max_length=25)
    Department : str = Field(min_length=1 , max_length=51)
    Credit : int = Field(ge=1 , le=4)


class courseregister(BaseModel):

    # CID = UUID
    CName: str = Field(min_length=1, max_length=25)
    Department: str = Field(min_length=1, max_length=51)
    Credit: int = Field(ge=1, le=4)
    # STID = UUID
    FName: str = Field(min_length=1, max_length=10)
    LName: str = Field(min_length=1, max_length=10)

class presentedcourses(BaseModel):

    # CID = UUID
    CName: str = Field(min_length=1, max_length=25)
    Department: str = Field(min_length=1, max_length=51)
    Credit: int = Field(ge=1, le=4)
    # LID : UUID
    FName: str = Field(min_length=1, max_length=10)
    LName: str = Field(min_length=1, max_length=10)


@app.get("/Data/Read/")
async def read_university_database(db: Session = Depends(get_db)):
    students = db.query(models.myModels.Student).all()
    lecturers = db.query(models.myModels.lecturer).all()
    courses = db.query(models.myModels.course).all()
    courseregister = db.query(models.myModels.courseregister).all()
    presentedcourses = db.query(models.myModels.presentedcourses).all()
    return {
        "students": students,
        "lecturers": lecturers,
        "courses": courses,
        "courseregister":courseregister,
        "presentedcourses":presentedcourses
    }

@app.post("/Data/Create/")
async def create_university_database(Stu:Student , lec=lecturer , cor=course , cr=courseregister , pres=presentedcourses , db:Session=Depends(get_db)):

    student_db = db.query(models.myModels.Student)
    lecturer_db = db.query(models.myModels.lecturer)
    course_db = db.query(models.myModels.course)
    courseregister_db = db.query(models.myModels.courseregister)
    presentedcourses_db = db.query(models.myModels.presentedcourses)

    student_db.FName = Stu.FName
    student_db.LName = Stu.LName
    student_db.Father = Stu.Father
    student_db.Birth = Stu.Birth
    student_db.IDS = Stu.IDS
    student_db.BornCity = Stu.BornCity
    student_db.Address = Stu.Address
    student_db.PostalCode = Stu.PostalCode
    student_db.CPhone = Stu.CPhone
    student_db.HPhone = Stu.HPhone
    student_db.Department = Stu.Department
    student_db.Major = Stu.Major
    student_db.Married = Stu.Married
    student_db.ID = Stu.ID

    db.add(student_db)
    db.commit()

    lecturer_db.FName = lec.FName
    lecturer_db.LName = lec.LName
    lecturer_db.ID = lec.ID
    lecturer_db.Department = lec.Department
    lecturer_db.Major = lec.Major
    lecturer_db.Birth = lec.Birth
    lecturer_db.BornCity = lec.BornCity
    lecturer_db.Address = lec.Address
    lecturer_db.PostalCode = lec.PostalCode
    lecturer_db.CPhone = lec.CPhone
    lecturer_db.HPhone = lec.HPhone

    db.add(lecturer_db)
    db.commit()

    course_db.CID = cor.CID
    course_db.CName = cor.CName
    course_db.Department = cor.Department
    course_db.Credit = cor.Credit

    db.add(course_db)
    db.commit()

    courseregister_db.CName = cr.CName
    courseregister_db.Department = cr.Department
    courseregister_db.Credit = cr.Credit
    courseregister_db.FName = cr.FName
    courseregister_db.LName = cr.LName

    db.add(courseregister_db)
    db.commit()

    presentedcourses_db.CName = pres.CName
    presentedcourses_db.Department = pres.Department
    presentedcourses_db.Credit = pres.Credit
    presentedcourses_db.FName = pres.FName
    presentedcourses_db.LName = pres.LName

    db.add(presentedcourses_db)
    db.commit()



@app.put("/Data/Update/")
async def update_university_database(s_id:int , l_id:int , c_id:int , correg_id:int , p_id:int , Stu:Student , lec=lecturer , cor=course , correg=courseregister , pres=presentedcourses , db:Session=Depends(get_db)):

    student_db = db.query(models.myModels.Student).filter(models.myModels.Student.STID == s_id).first()
    lecturer_db = db.query(models.myModels.lecturer).filter(models.myModels.lecturer.LID == l_id).first()
    course_db = db.query(models.myModels.course).filter(models.myModels.course.CID == c_id).first()
    courseregister_db = db.query(models.myModels.courseregister).filter(models.myModels.courseregister.CID == correg_id).first()
    presentedcourses_db = db.query(models.myModels.presentedcourses).filter(models.myModels.presentedcourses.CID == p_id).filter()

    if student_db is None:
        raise HTTPException(status_code=404 , detail="\n\n please enter the valid amount for student...!!!")
    else:
        student_db.FName = Stu.FName
        student_db.LName = Stu.LName
        student_db.Father = Stu.Father
        student_db.Birth = Stu.Birth
        student_db.IDS = Stu.IDS
        student_db.BornCity = Stu.BornCity
        student_db.Address = Stu.Address
        student_db.PostalCode = Stu.PostalCode
        student_db.CPhone = Stu.CPhone
        student_db.HPhone = Stu.HPhone
        student_db.Department = Stu.Department
        student_db.Major = Stu.Major
        student_db.Married = Stu.Married
        student_db.ID = Stu.ID

    db.add(student_db)
    db.commit()

    if lecturer_db is None:
        raise HTTPException(status_code=404 , detail="\n\n please enter the valid amount for lecturer...!!!")
    else:
        lecturer_db.FName = lec.FName
        lecturer_db.LName = lec.LName
        lecturer_db.ID = lec.ID
        lecturer_db.Department = lec.Department
        lecturer_db.Major = lec.Major
        lecturer_db.Birth = lec.Birth
        lecturer_db.BornCity = lec.BornCity
        lecturer_db.Address = lec.Address
        lecturer_db.PostalCode = lec.PostalCode
        lecturer_db.CPhone = lec.CPhone
        lecturer_db.HPhone = lec.HPhone

    db.add(lecturer_db)
    db.commit()

    if course_db is None:
        raise HTTPException(status_code=404 , detail="\n\n please enter the valid amount for course...!!!")
    else:
        course_db.CID = cor.CID
        course_db.CName = cor.CName
        course_db.Department = cor.Department
        course_db.Credit = cor.Credit

    db.add(course_db)
    db.commit()

    if courseregister_db is None:
        raise HTTPException(status_code=404 , detail="\n\n please enter the valid amount for course register...!!!")
    else:
        courseregister_db.CName = correg.CName
        courseregister_db.Department = correg.Department
        courseregister_db.Credit = correg.Credit
        courseregister_db.FName = correg.FName
        courseregister_db.LName = correg.LName

    db.add(courseregister_db)
    db.commit()

    if presentedcourses_db is None:
        raise HTTPException(status_code=404 , detail="\n\n please enter the valid amount for presented courses...!!!")
    else:
        presentedcourses_db.CName = pres.CName
        presentedcourses_db.Department = pres.Department
        presentedcourses_db.Credit = pres.Credit
        presentedcourses_db.FName = pres.FName
        presentedcourses_db.LName = pres.LName

    db.add(presentedcourses_db)
    db.commit()

    return {"student":Stu , "lecturer":lec , "course":cor , "courseRegister":correg , "presentedCourses":pres}

@app.delete("/Data/Delete/")
async def delete_university_database(s_id:int , l_id:int , c_id:int , correg_id:int , p_id:int , db:Session=Depends(get_db)):

    student_db = db.query(models.myModels.Student).filter(models.myModels.Student.STID == s_id).first()
    lecturer_db = db.query(models.myModels.lecturer).filter(models.myModels.lecturer.LID == l_id).first()
    course_db = db.query(models.myModels.course).filter(models.myModels.course.CID == c_id).first()
    courseregister_db = db.query(models.myModels.courseregister).filter(models.myModels.courseregister.CID == correg_id).first()
    presentedcourses_db = db.query(models.myModels.presentedcourses).filter(models.myModels.presentedcourses.CID == p_id).filter()

    if student_db is not None:
        db.query(models.myModels.Student).filter(models.myModels.Student.STID == s_id).delete()
        db.commit()
    else:
        raise HTTPException(status_code=404 , detail="\n\n please enter the valid amount for student...!!!")

    if lecturer_db is not None:
        db.query(models.myModels.lecturer).filter(models.myModels.lecturer.LID == l_id).delete()
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="\n\n please enter the valid amount for lecturer...!!!")

    if course_db is not None:
        db.query(models.myModels.course).filter(models.myModels.course.CID == c_id).delete()
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="\n\n please enter the valid amount for student...!!!")

    if courseregister_db is not None:
        db.query(models.myModels.courseregister).filter(models.myModels.courseregister.CID == correg_id).delete()
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="\n\n please enter the valid amount for student...!!!")

    if presentedcourses_db is not None:
        db.query(models.myModels.presentedcourses).filter(models.myModels.presentedcourses.CID == p_id).delete()
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="\n\n please enter the valid amount for student...!!!")


