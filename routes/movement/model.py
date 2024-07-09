import uuid
from routes.database import Base
from sqlalchemy import Column, UUID, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Movement(Base):
    __tablename__ = "movement"
    id = Column(UUID, primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    date = Column(DateTime)
    id_payment_method = Column(UUID, ForeignKey("payment_method.id", ondelete="CASCADE"))
    id_movement_type = Column(UUID, ForeignKey("movement_type.id", ondelete="CASCADE"))
    id_movement_category = Column(UUID, ForeignKey("movement_category.id", ondelete="CASCADE"))
    id_account = Column(UUID, ForeignKey("account.id"))

    payment_method = relationship("PaymentMethod")
    movement_type = relationship("MovementType")
    movement_category = relationship("MovementCategory")

    def dict(self):
        return {
            "id": self.id.__str__(),
            "date": self.date,
            "id_payment_method": self.id_payment_method,
            "id_movement_type": self.id_movement_type,
            "id_movement_category": self.id_movement_category,
            "id_account": self.id_account,
            "payment_method": self.payment_method.dict() if self.payment_method else None,
            "movement_type": self.movement_type.dict() if self.movement_type else None,
            "movement_category": self.movement_category.dict() if self.movement_category else None,
        }

