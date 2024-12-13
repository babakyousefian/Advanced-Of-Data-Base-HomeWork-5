from database.myDatabase import Base
from sqlalchemy import Column, String, Date, Integer, Boolean, BigInteger
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy import PrimaryKeyConstraint

class Student(Base):
    __tablename__ = "student"

    STID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True, unique=True)
    FName = Column(String, nullable=False)
    LName = Column(String, nullable=False)
    Father = Column(String, nullable=False)
    Birth = Column(Date, nullable=False)
    IDS = Column(String, nullable=False)
    BornCity = Column(String, nullable=False)
    Address = Column(String, nullable=False)
    PostalCode = Column(BigInteger, nullable=False)
    CPhone = Column(String, nullable=False)
    HPhone = Column(String, nullable=False)
    Department = Column(String, nullable=False)
    Major = Column(String, nullable=False)
    Married = Column(Boolean, nullable=False)
    ID = Column(String, nullable=False)
class lecturer(Base):

    __tablename__ = "lecturer"

    LID = Column(Integer , primary_key=True , index=True , unique=True , nullable=False)
    FName = Column(String , nullable=False)
    LName = Column(String , nullable=False)
    ID = Column(String , nullable=False)
    Department = Column(String , nullable=False)
    Major = Column(String , nullable=False)
    Birth = Column(Date , nullable=False)
    BornCity = Column(String , nullable=False)
    Address = Column(String , nullable=False)
    PostalCode = Column(BigInteger , nullable=False)
    CPhone = Column(String , nullable=False)
    HPhone = Column(String , nullable=False)



class course(Base):

    __tablename__ = "course"

    CID = Column(Integer , primary_key=True , index=True , nullable=False , unique=True)
    CName = Column(String , nullable=False)
    Department = Column(String , nullable=False)
    Credit = Column(Integer , nullable=False)


class courseregister(Base):

    __tablename__ = "CourseRegister"

    __table_args__ = (
        PrimaryKeyConstraint('CID', 'SID'),
    )

    CID = Column(Integer, primary_key=True, index=True , unique=True , nullable=False)
    CName = Column(String , nullable=False)
    Department = Column(String , nullable=False)
    Credit = Column(Integer , nullable=False)
    SID = Column(Integer, primary_key=True, index=True , unique=True , nullable=False)
    FName = Column(String , nullable=False)
    LName = Column(String , nullable=False)



class presentedcourses(Base):

    __tablename__ = "PresentedCourses"

    CID = Column(Integer, primary_key=True, index=True , unique=True , nullable=False)
    CName = Column(String , nullable=False)
    Department = Column(String , nullable=False)
    Credit = Column(Integer , nullable=False)
    LID = Column(Integer, primary_key=True, index=True , unique=True , nullable=False)
    FName = Column(String , nullable=False)
    LName = Column(String , nullable=False)

