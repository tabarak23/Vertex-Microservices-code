from fastapi import HTTPException, status
from app.repository.user_repository import UserRepository
from app.schemas.user_dto import UserCreateRequest

class UserService:

    @staticmethod
    def create_user(req: UserCreateRequest):
        # Business rule: email must be unique
        if UserRepository.email_exists(req.email):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already exists"
            )

        return UserRepository.create(req)

    @staticmethod
    def get_user(user_id: int):
        user = UserRepository.get_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return user

    @staticmethod
    def list_users():
        return UserRepository.list_all()

    @staticmethod
    def deactivate_user(user_id: int):
        user = UserRepository.get_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        UserRepository.deactivate(user_id)
