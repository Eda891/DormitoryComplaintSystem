from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from dependencies import get_db, get_current_admin
from models import Complaint,User
from schemas import ComplaintResponse, ComplaintUpdate
router = APIRouter()

# View all incoming complaints
@router.get("/complaints",response_model=List[ComplaintResponse])
def get_all_complaints(db:Session=Depends(get_db), current_admin:User=Depends(get_current_admin)):
          return db.query(Complaint).all()

# Update complaint (assign staff, status, etc.)
@router.patch("/complaints/{complaint_id}", response_model=ComplaintResponse)
def update_complaint(
        complaint_id:int,
        update: ComplaintUpdate,
        db: Session = Depends(get_db),
        current_admin: User=Depends(get_current_admin)
):
          complaint=db.query(Complaint).filter(Complaint.id==complaint_id).first()
          if not complaint:
                  raise HTTPException(status_code=404,detail="Complaint not found")
          if update.status:
                  complaint.status=update.status
                  if update.status=="resolved":
                          complaint.resolved_at=datetime.utcnow()
          if update.assignedStaff:
                  complaint.assignedStaff=update.assignedStaff
          if update.estimatedVisit:
                  complaint.estimatedVisit=update.estimatedVisit
          db.commit()
          db.refresh
          return complaint