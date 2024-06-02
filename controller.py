from .model import User,Student
from . import db
import uuid
class StudentController:
    def addStudent(self,userDetail:dict)->str:
        user = userDetail["user"]
        detail = userDetail["detail"]
        try:
            newuser = User(**user)
            detail = Student(**detail)
        except Exception as e:
            return str(e)
        detail.detail = newuser
        db.session.add(newuser)
        db.session.add(detail)
        db.session.commit()
        return 'success'
    
    def getStudent(self,studentID:str)->Student:
        return db.session.query(Student).join(User).filter(User.userid.is_(studentID)).first()

studentController = StudentController()
    
