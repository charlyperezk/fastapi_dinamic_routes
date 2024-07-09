from examples.movement_category.model import MovementCategory
from examples.movement_type.model import MovementType
from examples.payment_method.model import PaymentMethod
from examples.movement.model import Movement
import uuid, datetime
from examples.database import get_session
from router_manager import db


def first_config():
    session = get_session()
    mc_client = db.CRUDController(model=MovementCategory)
    mt_client = db.CRUDController(model=MovementType)
    pm_client = db.CRUDController(model=PaymentMethod)
    m_client = db.CRUDController(model=Movement)

    mc1 = MovementCategory(id=uuid.uuid4(), name="Food", description="Food", default=True)
    mc_client.create(mc1, session)
    mc2 = MovementCategory(id=uuid.uuid4(), name="Others", description="Others", default=True)
    mc_client.create(mc2, session)


    mt1 = MovementType(id=uuid.uuid4(), name="Income", description="Income", default=True)
    mt_client.create(mt1, session)
    mt2 = MovementType(id=uuid.uuid4(), name="Expense", description="Expense", default=True)
    mt_client.create(mt2, session)

    pm1 = PaymentMethod(id=uuid.uuid4(), name="Card", description="Card", default=True)
    pm_client.create(pm1, session)
    pm2 = PaymentMethod(id=uuid.uuid4(), name="Cash", description="Cash", default=True)
    pm_client.create(pm2, session)

    m1 = Movement(id=uuid.uuid4(), date=datetime.datetime.now(), id_payment_method=pm1.id, id_movement_type=mt1.id, id_movement_category=mc1.id)
    m_client.create(m1, session)    
    m2 = Movement(id=uuid.uuid4(), date=datetime.datetime.now(), id_payment_method=pm2.id, id_movement_type=mt2.id, id_movement_category=mc2.id)
    m_client.create(m2, session)

