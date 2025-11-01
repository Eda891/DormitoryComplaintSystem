from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"
    userName = Column(String, unique=True)
    studentİd = Column(Integer,primary_key=True)
    email = Column(String, unique=True)
    phone=Column(Integer,unique=True)
    roomNum=Column(Integer,unique=True)
    password_hash = Column(String)
    Registrated=Column(bool)
    RegistratedOn = Column(datetime) 
    
    complaints = relationship("Complaint", back_populates="student")

class Complaint(Base):
    __tablename__ = "complaints"
    complaintİd=Column(String, primary_key=True, index=True)
    studentİd = Column(Integer, ForeignKey("users.id"))
    title = Column(String)
    description = Column(String)
    note = Column(String)
    category=Column(Integer)
    status=Column(bool)
    studentName= Column(String, unique=True)
    email = Column(String, unique=True)
    phone=Column(Integer,unique=True)
    roomNum=Column(Integer,unique=True)
    submissionDate = Column(datetime) 
    assignedStaff=Column(String, unique=True)
    department=Column(String, unique=True)
    estimatedVisit=Column(datetime)
    contactİnfo=Column(Integer,unique=True)

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    