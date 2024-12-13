
from pydantic import BaseModel , Field

class student(BaseModel):

    FName : str = Field(min_length=1 , max_length=10)
    LName : str = Field(min_length=1 , max_length=10)
    Father : str = Field(min_length=1 , max_length=10)
    Birth : str = Field(min_length=1 , max_length=10)
    IDS : str = Field(min_length=11 , max_length=11)
    BornCity : str = Field(min_length=1 , max_length=51)
    Address : str = Field(min_length=1 , max_length=100)
    PostalCode : str = Field(min_length=10 , max_length=10)
    CPhone : str = Field(min_length=11 , max_length=11)
    HPhone : str = Field(min_length=11 , max_length=11)
    Department : str = Field(min_length=1 , max_length=100)
    Major : str = Field(min_length=1 , max_length=100)
    Married : bool
    ID : str = Field(min_length=11 , max_length=11)


class lecturer(BaseModel):

    FName: str = Field(min_length=1, max_length=10)
    LName: str = Field(min_length=1, max_length=10)
    ID: str = Field(min_length=11, max_length=11)
    Department: str = Field(min_length=1, max_length=100)
    Major: str = Field(min_length=1, max_length=100)
    Birth: str = Field(min_length=1, max_length=10)
    BornCity: str = Field(min_length=1, max_length=51)
    Address: str = Field(min_length=1, max_length=100)
    PostalCode: str = Field(min_length=10, max_length=10)
    CPhone: str = Field(min_length=11, max_length=11)
    HPhone: str = Field(min_length=11, max_length=11)


class course(BaseModel):

    CName : str = Field(min_length=1 , max_length=25)
    Department : str = Field(min_length=1 , max_length=51)
    Credit : int = Field(gt=1 , le=4)

class CourseRegister(BaseModel):

    CName: str = Field(min_length=1, max_length=25)
    Department: str = Field(min_length=1, max_length=51)
    Credit: int = Field(gt=1, le=4)
    FName: str = Field(min_length=1, max_length=10)
    LName: str = Field(min_length=1, max_length=10)

class PresentedCourses(BaseModel):

    CName: str = Field(min_length=1, max_length=25)
    Department: str = Field(min_length=1, max_length=51)
    Credit: int = Field(gt=1, le=4)
    FName: str = Field(min_length=1, max_length=10)
    LName: str = Field(min_length=1, max_length=10)

