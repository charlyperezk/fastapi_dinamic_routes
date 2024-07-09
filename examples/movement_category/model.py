import uuid
from sqlalchemy.orm import relationship
from examples.database import Base
from sqlalchemy import Column, String, Boolean, UUID, Integer


class MovementCategory(Base):
    __tablename__ = "movement_category"
    id = Column(UUID, primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String)
    description = Column(Integer)
    default = Column(Boolean, default=False)
    movement = relationship("Movement", back_populates="movement_category")

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "default": self.default
        }

