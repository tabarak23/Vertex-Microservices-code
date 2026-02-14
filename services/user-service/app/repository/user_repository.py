from app.db.session import SessionLocal
from app.models.user_model import User
from app.schemas.user_dto import UserResponse
from sqlalchemy.orm import Session


class UserRepository:

    @staticmethod
    def create(req):
        db: Session = SessionLocal()
        try:
            user = User(
                email=req.email,
                name=req.name,
                status="ACTIVE"   # IMPORTANT: default lifecycle state
            )
            db.add(user)
            db.commit()
            db.refresh(user)
            return UserResponse.from_orm(user)
        finally:
            db.close()

    @staticmethod
    def get_by_id(user_id: int):
        db: Session = SessionLocal()
        try:
            user = (
                db.query(User)
                .filter(User.id == user_id, User.status == "ACTIVE")
                .first()
            )
            return UserResponse.from_orm(user) if user else None
        finally:
            db.close()

    @staticmethod
    def list_all():
        db: Session = SessionLocal()
        try:
            users = (
                db.query(User)
                .filter(User.status == "ACTIVE")
                .all()
            )
            return [UserResponse.from_orm(u) for u in users]
        finally:
            db.close()

    @staticmethod
    def deactivate(user_id: int):
        db: Session = SessionLocal()
        try:
            db.query(User).filter(User.id == user_id).update(
                {"status": "INACTIVE"}
            )
            db.commit()
        finally:
            db.close()

    @staticmethod
    def email_exists(email: str) -> bool:
        db: Session = SessionLocal()
        try:
            return (
                db.query(User)
                .filter(User.email == email)
                .first()
                is not None
            )
        finally:
            db.close()
