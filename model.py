from . import db
from sqlalchemy.orm import mapped_column, Mapped,relationship
import sqlalchemy as sa
import uuid
import datetime


class User(db.Model):
    __tablename__ = 'users'
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    userid: Mapped[str] = mapped_column(sa.String(26), unique=True, nullable=False, index=True)
    username: Mapped[str] = mapped_column(sa.String(256), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(sa.String(256), nullable=False)
    email: Mapped[str] = mapped_column(sa.String(256), nullable=False, unique=True)
    createAt: Mapped[datetime.date] = mapped_column(sa.DATE, default=datetime.datetime.now().date)
    role: Mapped[str] = mapped_column(sa.String(256), nullable=False)
    firstName: Mapped[str] = mapped_column(sa.String(256), nullable=False)
    lastName: Mapped[str] = mapped_column(sa.String(256), nullable=False)
    student: Mapped["Student"] = relationship(back_populates='detail')
    teacher: Mapped["Teacher"] = relationship(back_populates='detail')
    


class Student(db.Model):
    __tablename__ = 'students'
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    grade: Mapped[int] = mapped_column(nullable=False)
    addmission_date: Mapped[datetime.date] = mapped_column(default=datetime.datetime.now().date)
    user_id: Mapped[uuid.UUID]  = mapped_column(sa.ForeignKey('users.id'),nullable=False)
    detail: Mapped["User"] = relationship(back_populates='student')

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    major: Mapped[str] = mapped_column(sa.String(256),nullable= False)
    subject: Mapped[str] = mapped_column(sa.String(256),nullable= False)
    user_id: Mapped[uuid.UUID]  = mapped_column(sa.ForeignKey('users.id'),nullable=False)
    detail: Mapped["User"] = relationship(back_populates='teacher')
