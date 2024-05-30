from . import db,metadata
from sqlalchemy.orm import mapped_column, Mapped,relationship
import sqlalchemy as sa
import uuid
import datetime
from typing import List

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
    student: Mapped["Student"] = relationship(back_populates='detail')
    teacher: Mapped["Teacher"] = relationship(back_populates='detail')
    
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
    detail: Mapped["User"] = relationship(back_populates='student')
    courses: Mapped[List["Course"]] = relationship(secondary=course_students,back_populates='student')

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    major: Mapped[str] = mapped_column(sa.String(256),nullable= False)
    subject: Mapped[str] = mapped_column(sa.String(256),nullable= False)
    user_id: Mapped[uuid.UUID]  = mapped_column(sa.ForeignKey('users.id'),nullable=False)
    detail: Mapped["User"] = relationship(back_populates='teacher')
    courses: Mapped[List["Course"]] = relationship(back_populates='teacher')

class Subject(db.Model):
    __tablename__ = 'subjects'
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True,default=uuid.uuid4)
    nameofSubject: Mapped[str] = mapped_column(sa.String(256),nullable=False)
    major: Mapped[str] = mapped_column(sa.String(256),nullable=False)
    courses: Mapped[List["CourseDetail"]] = relationship(back_populates='subject')


class CourseDetail(db.Model):
    __tablename__ = 'coursedetails'
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True,default=uuid.uuid4)
    inProgress: Mapped[bool] = mapped_column(primary_key=True,default=True)
    startDate: Mapped[datetime.date] = mapped_column(default=datetime.datetime.now().date())
    endDate: Mapped[datetime.date] = mapped_column(nullable=False)
    subject_id: Mapped[uuid.UUID] = mapped_column(sa.ForeignKey('subjects.id'),nullable=False)
    numberofStudent: Mapped[int] = mapped_column(default=0)
    maxStudent: Mapped[int] = mapped_column(default=50)
    subject: Mapped["Subject"] = relationship(back_populates='course')
    course: Mapped["Course"] = relationship(back_populates='course')

class Course(db.Model):
    __tablename__ = 'courses'
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True,default=uuid.uuid4)
    teacher_id: Mapped[uuid.UUID] = mapped_column(sa.ForeignKey('teachers.id'),nullable=False)
    courseDetail_id: Mapped[uuid.UUID] = mapped_column(sa.ForeignKey('coursedetails.id'),nullable=False)
    courseDetail: Mapped["CourseDetail"] = relationship(back_populates='course') 
    teacher: Mapped["Teacher"] = relationship(back_populates='course')