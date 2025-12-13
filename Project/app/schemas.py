from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
# User Schemas
class UserCreate(BaseModel):
          studentİd: str
          userName:str
          email:EmailStr
          phone:Optional[str] = None
          roomNum:str
          password_hash:str
class UserResponse(BaseModel):
        id:int
        student_id:str
        email:EmailStr
        phone:Optional[str]
        roomNum:str
        submissionDate:datetime

        class Config:
                from_attributes=True
class Token(BaseModel):
        access_token:str
        token_type:str

# Complaint Schemas
class ComplaintCreate(BaseModel):
        title:str
        description:str
        category_id: int
class ComplaintResponse(BaseModel):
        id:int
        title:str
        description:str
        image_url: Optional[str]
        status:str
        submissionDate:datetime
        resolved_at: datetime
        category_id: int
        student_id: int
        
        class Config:
                from_attributes=True
class ComplaintUpdate(BaseModel):
        status: Optional[str] = None
        assignedStaff:Optional[str] = None
        estimatedVisit: Optional[datetime] = None

# Category Schemas
class CategoryCreate(BaseModel):
    name: str

class CategoryResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

# Rating Schemas
class RatingCreate(BaseModel):
       id: int
       rating:int
       comment: Optional[str]
       created_at: datetime
       complaint_id: int

class RatingResponse(BaseModel):
    id: int
    score: int
    comment: Optional[str]
    created_at: datetime
    complaint_id: int
       
class Config:
        from_attributes = True


                   