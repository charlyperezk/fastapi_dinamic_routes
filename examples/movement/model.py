import uuid
from examples.database import Base
from sqlalchemy import Column, Boolean, UUID, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from examples.payment_method.model import PaymentMethod
from examples.movement_type.model import MovementType
from examples.movement_category.model import MovementCategory


class Movement(Base):
    __tablename__ = "movement"
    id = Column(UUID, primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    date = Column(DateTime)
    id_payment_method = Column(UUID, ForeignKey("payment_method.id"))
    id_movement_type = Column(UUID, ForeignKey("movement_type.id"))
    id_movement_category = Column(UUID, ForeignKey("movement_category.id"))
    payment_method = relationship("PaymentMethod", back_populates="movement")
    movement_type = relationship("MovementType", back_populates="movement")
    movement_category = relationship("MovementCategory", back_populates="movement")

    def dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "id_payment_method": self.id_payment_method,
            "id_movement_type": self.id_movement_type,
            "id_movement_category": self.id_movement_category,
            "payment_method": self.payment_method,
            "movement_type": self.movement_type,
            "movement_category": self.movement_category
        }

