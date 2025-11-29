from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    userName = Column(String, unique=True,nullable=False,index=True)
    studentİd = Column(Integer,unique=True,nullable=False,index=True)
    email = Column(String, unique=True,index=True, nullable=False)
    phone=Column(String,unique=True)
    roomNum=Column(Integer,nullable=False)
    password_hash = Column(String,nullable=False)
    is_active=Column(Boolean,default=True)
    registered_at = Column(DateTime,default=datetime.now) 
    
    complaints = relationship("Complaint", back_populates="student")
    ratings = relationship("Rating", back_populates="student")

class Complaint(Base):
    __tablename__ = "complaints"
    id = Column(Integer, primary_key=True, index=True)
    # complaintİd=Column(String, primary_key=True, index=True)
    # studentİd = Column(Integer, ForeignKey("users.id"))
    title = Column(String,nullable=False)
    description = Column(Text,nullable=False)
    image_url = Column(String, nullable=True)
    status=Column(String,default="pending")
    submissionDate = Column(DateTime,default=datetime.now) 
    resolved_at = Column(DateTime, nullable=True)
    # note = Column(String,nullable=False)
    # category=Column(Integer,nullable=False)
    # studentName= Column(String, unique=True)
    # email = Column(String, unique=True)
    # phone=Column(Integer,unique=True)
    # roomNum=Column(Integer,unique=True)
    assignedStaff=Column(String, unique=True)
    # department=Column(String, unique=True)
    estimatedVisit=Column(DateTime,nullable=True)

    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    student = relationship("User", back_populates="complaints")
    category = relationship("Category", back_populates="complaints")
    rating = relationship("Rating", back_populates="complaint", uselist=False)

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True,index=True, nullable=False)

    complaints = relationship("Complaint", back_populates="category")

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True)
    rating = Column(Integer, nullable=False) 
    comment = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.now)

    complaint_id = Column(Integer, ForeignKey("complaints.id"), unique=True)
    student_id = Column(Integer, ForeignKey("users.id"))

    complaint = relationship("Complaint", back_populates="rating")
    student = relationship("User", back_populates="ratings")   
    