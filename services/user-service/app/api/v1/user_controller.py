from fastapi import APIRouter, HTTPException
from app.schemas.user_dto import UserCreateRequest, UserResponse
from app.service.user_service import UserService

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_user(req: UserCreateRequest):
    return UserService.create_user(req)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    user = UserService.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=list[UserResponse])
def list_users():
    return UserService.list_users()

@router.delete("/{user_id}")
def deactivate_user(user_id: int):
    UserService.deactivate_user(user_id)
    return {"status": "deactivated"}

