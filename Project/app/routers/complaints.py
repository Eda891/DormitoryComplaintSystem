from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import os
from ..dependencies import get_db, get_current_user
from ..models import Complaint, Rating, User
from ..schemas import ComplaintCreate, ComplaintResponse, RatingCreate, RatingResponse
router = APIRouter()

# Submit complaint
@router.post("/", response_model=ComplaintResponse)
def submit_complaint(
    complaint: ComplaintCreate,
    photo: UploadFile = File(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_complaint=Complaint(**complaint.dict(), studentİd=current_user.id)
    if photo:
        # Save photo (simple file save; use S3 in production)
        photo_path=f"uploads/{photo.filename}"
        os.makedirs("uploads",exist_ok=True)
        with open(photo_path,"wb") as f:
            f.write(photo.file.read())
        new_complaint.photo_url=photo_path
    db.add(new_complaint)
    db.commit()
    db.refresh(new_complaint)
    return new_complaint

#List my complaints
@router.get("/my", response_model=List[ComplaintResponse])
def get_my_complaints(
    db: Session=Depends(get_db),
    current_user:User=Depends(get_current_user)
):
    return db.query(Complaint).filter(Complaint.student_id==current_user.id).all()

#Rate a resolved complaint
@router.post("/{complaint_id}/rate",response_model=RatingResponse)
def rate_complaint(
    complaint_id: int,
    rating:RatingCreate,
    db: Session=Depends(get_db),
    current_user: User=Depends(get_current_user)
):
    complaint=db.query(Complaint).filter(Complaint.id==complaint_id).all()
    if not complaint or complaint.student_id !=current_user.id:
        raise HTTPException(status_code=404, detail="Complaint not found")
    if complaint.status != "resolved":
        raise HTTPException(status_code=400, detail="Can only rate resolved complaints")
    if complaint.rating:
        raise HTTPException(status_code=400, detail="Already rated")
    new_rating = Rating(**rating.dict(), complaint_id=complaint_id, student_id=current_user.id)
    db.add(new_rating)
    db.commit()
    db.refresh(new_rating)
    return new_rating
