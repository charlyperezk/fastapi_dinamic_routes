from examples.database import Base
from sqlalchemy import Column, String, Boolean, UUID, Integer
import uuid


class User(Base):
    __tablename__ = "user"
    id = Column(UUID, primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String)
    age = Column(Integer)
    # is_default = Column(Boolean, default=False)
    # is_active = Column(Boolean, default=True)

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            # "is_active": self.is_active
        }

