import uuid
import datetime
from sqlalchemy.orm import relationship
from routes.database import Base
from sqlalchemy import Column, String, DateTime, UUID, Integer


class Account(Base):
    __tablename__ = "account"
    id = Column(UUID, primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    name = Column(String)
    description = Column(Integer)

    movements = relationship("Movement", cascade='all, delete-orphan')

    def dict(self):
        return {
            "id": self.id.__str__(),
            "created_at": self.created_at,
            "name": self.name,
            "description": self.description,
            "movements": [movement.dict() for movement in self.movements]
        }