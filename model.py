from . import db
from sqlalchemy.orm import mapped_column,Mapped
import sqlalchemy as sa
import uuid
import datetime

class User(db.Model):
    __table__ = 'users'
    id : Mapped[uuid.UUID] = mapped_column(primary_key=True,default=uuid.uuid4)
    userid: Mapped[str] = mapped_column(sa.String(26),unique=True,nullable=False,index=True)
    username: Mapped[str] = mapped_column(sa.String(256),unique= True,nullable= False)
    password: Mapped[str] = mapped_column(sa.String(256),nullable=False)
    email: Mapped[str] = mapped_column(sa.String(256),nullable=False,unique=True)
    createAt: Mapped[datetime.date] = mapped_column(sa.DATE,default=datetime.datetime.now().date)
    role: Mapped[str] = mapped_column(sa.String(256),nullable=False)
    firstName: Mapped[str] = mapped_column(sa.String(256),nullable=False)
    lastName: Mapped[str] = mapped_column(sa.String(256),nullable=False)


class Student(db.Model):
    __table__ = 'students'
    id : Mapped[uuid.UUID] = mapped_column(primary_key=True,default=uuid.uuid4)
    
