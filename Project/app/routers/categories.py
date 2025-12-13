from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from dependencies import get_db, get_current_admin
from models import Category,User
from schemas import CategoryCreate, CategoryResponse

router = APIRouter()

@router.post("/",response_model=CategoryResponse)
def create_category(
          category:CategoryCreate,
          db:Session=Depends(get_db),
          current_admin:User=Depends(get_current_admin)
):
          existing=db.query(Category).filter(Category.name==category.name).first()
          if existing:
              raise HTTPException(status_code=400,detail="Category exists")
          new_category=Category(**category.dict())
          db.add(new_category)
          db.commit()
          db.refresh(new_category)
          return new_category
@router.get("/",response_model=List[CategoryResponse])
def get_categories(db:Session=Depends(get_db)):
       return db.query(Category).all()

@router.delete("/{category_id}")
def delete_category(
  category_id=int,
  db:Session=Depends(get_db),
  current_admin:User=Depends(get_current_admin)     
):
       category=db.query(Category).filter(Category.id==category_id).first()
       if not category:
              raise HTTPException(status_code=404, detail="Catgeroy not found")
       db.delete(category)
       db.commit
       return {"detail": "Category deleted"}