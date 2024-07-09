import uuid
from sqlalchemy.orm import relationship
from routes.database import Base
from sqlalchemy import Column, String, Boolean, UUID, Integer


class MovementCategory(Base):
    __tablename__ = "movement_category"
    id = Column(UUID, primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String)
    description = Column(Integer)
    default = Column(Boolean, default=False)
    movement = relationship("Movement", back_populates="movement_category", cascade='all, delete-orphan')

    def dict(self):
        return {
            "id": self.id.__str__(),
            "name": self.name,
            "description": self.description,
            "default": self.default
        }

