import uuid
from sqlalchemy.orm import relationship
from examples.database import Base
from sqlalchemy import Column, String, Boolean, UUID, Integer


class MovementType(Base):
    __tablename__ = "movement_type"
    id = Column(UUID, primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String)
    description = Column(Integer)
    default = Column(Boolean, default=False)
    movement = relationship("Movement", back_populates="movement_type")

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "default": self.default
        }

