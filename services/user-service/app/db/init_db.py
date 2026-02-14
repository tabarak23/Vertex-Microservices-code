from app.db.session import engine
from app.db.base import Base

# Import models so Base knows about them
from app.models.user_model import User  # noqa


def init_db():
    Base.metadata.create_all(bind=engine)
