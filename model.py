from . import db,metadata
from sqlalchemy.orm import mapped_column, Mapped,relationship
import sqlalchemy as sa
import uuid
import datetime
from typing import List
import re

class User(db.Model):
    __tablename__ = 'users'
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    userid: Mapped[str] = mapped_column(sa.String(26), unique=True, nullable=False, index=True)
    username: Mapped[str] = mapped_column(sa.String(256), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(sa.String(256), nullable=False)
    email: Mapped[str] = mapped_column(sa.String(256), nullable=False, unique=True)
    createAt: Mapped[datetime.date] = mapped_column(sa.DATE, default=datetime.datetime.now().date())
    role: Mapped[str] = mapped_column(sa.String(256), nullable=False)
    firstName: Mapped[str] = mapped_column(sa.String(256), nullable=False)
    lastName: Mapped[str] = mapped_column(sa.String(256), nullable=False)
    student: Mapped["Student"] = relationship(backref='detail')
    teacher: Mapped["Teacher"] = relationship(backref='detail')

    def setPassword(self,password:str)->None:
        if(len(password)<8): 
            raise RuntimeError('length password must longer than 8')
        self.password = password
    
    def setUserName(self,username:str)->None:
        user = db.session.query(User).filter(User.username.is_(username)).first()
        if(user != None):
            raise RuntimeError('username unvalid')
        self.username = username
    
    def setEmail(self,email:str)->None:
        if(not email.endswith('@gmail.com')):
            raise RuntimeError('Unvalid Email')
        self.email = email

    def __init__(self,
                 userid:str,
                 username:str,password:str,
                 email:str,role:str,
                 firstname:str,
                 lastname:str) -> None:
        self.userid = userid
        self.setUserName(username)
        self.setPassword(password)
        self.setEmail(email)
        self.firstName = firstname
        self.lastName = lastname
        self.role = role

    
course_students = sa.Table('course_students',metadata,
                           
                           sa.Column('id',sa.Uuid,primary_key=True),
                           sa.Column('studentid',sa.Uuid,sa.ForeignKey('students.id'),nullable=False),
                           sa.Column('courseid',sa.Uuid,sa.ForeignKey('courses.id'),nullable=False))

class Student(db.Model):
    __tablename__ = 'students'
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    grade: Mapped[int] = mapped_column(nullable=False)
    addmission_date: Mapped[datetime.date] = mapped_column(default=datetime.datetime.now().date())
    user_id: Mapped[uuid.UUID]  = mapped_column(sa.ForeignKey('users.id'),nullable=False)


    def __init__(self,grade:int,addmission_date:datetime.date,user:User) -> None:
        self.grade = grade
        self.addmission_date = addmission_date
        self.detail = user
        
    

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    major: Mapped[str] = mapped_column(sa.String(256),nullable= False)
    subject: Mapped[str] = mapped_column(sa.String(256),nullable= False)
    user_id: Mapped[uuid.UUID]  = mapped_column(sa.ForeignKey('users.id'),nullable=False)
    courses: Mapped[List["Course"]] = relationship(backref='teachercourse')

class Subject(db.Model):
    __tablename__ = 'subjects'
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True,default=uuid.uuid4)
    nameofSubject: Mapped[str] = mapped_column(sa.String(256),nullable=False)
    major: Mapped[str] = mapped_column(sa.String(256),nullable=False)
    courses: Mapped[List["CourseDetail"]] = relationship(backref='subject')


class CourseDetail(db.Model):
    __tablename__ = 'coursedetails'
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True,default=uuid.uuid4)
    inProgress: Mapped[bool] = mapped_column(primary_key=True,default=True)
    startDate: Mapped[datetime.date] = mapped_column(default=datetime.datetime.now().date())
    endDate: Mapped[datetime.date] = mapped_column(nullable=False)
    subject_id: Mapped[uuid.UUID] = mapped_column(sa.ForeignKey('subjects.id'),nullable=False)
    numberofStudent: Mapped[int] = mapped_column(default=0)
    maxStudent: Mapped[int] = mapped_column(default=50)
    course: Mapped["Course"] = relationship(backref='course')

class Course(db.Model):
    __tablename__ = 'courses'
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True,default=uuid.uuid4)
    teacher_id: Mapped[uuid.UUID] = mapped_column(sa.ForeignKey('teachers.id'),nullable=False)
    courseDetail_id: Mapped[uuid.UUID] = mapped_column(sa.ForeignKey('coursedetails.id'),nullable=False)
    students: Mapped[List["Student"]] = relationship(secondary=course_students,backref='courses')
