from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test():
    return {"msg": "Auth router is working!"}