from examples.database import Base
from sqlalchemy import Column, String, Boolean, UUID, Integer
from sqlalchemy.orm import relationship
import uuid


class PaymentMethod(Base):
    __tablename__ = "payment_method"
    id = Column(UUID, primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String)
    description = Column(Integer)
    default = Column(Boolean, default=False)
    movement = relationship("Movement", back_populates="payment_method")

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "default": self.default
        }

