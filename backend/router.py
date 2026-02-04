from fastapi import APIRouter, Response, Body, Depends, dependencies, HTTPException

router = APIRouter()

def get_current_user():
    return {"user_id": 1, "username": "testuser"}

@router.post("/create_item")
async def create_item(user: dict = Depends(get_current_user)):
    return {"message": "Item created successfully", "user id": user["user_id"]}