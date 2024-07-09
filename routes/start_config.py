from routes.movement_category.model import MovementCategory
from routes.movement_type.model import MovementType
from routes.payment_method.model import PaymentMethod
from routes.movement.model import Movement
from routes.account.model import Account
import uuid, datetime
from routes.database import get_session
from router_manager import db


def first_config():
    session = get_session()
    mc_client = db.CRUDController(model=MovementCategory)
    mt_client = db.CRUDController(model=MovementType)
    pm_client = db.CRUDController(model=PaymentMethod)
    m_client = db.CRUDController(model=Movement)
    a_client = db.CRUDController(model=Account)

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

    a1 = Account(id=uuid.uuid4(), name="Account 1", description="Account 1")
    a_client.create(a1, session)

    m1 = Movement(id=uuid.uuid4(), date=datetime.datetime.now(), id_payment_method=pm1.id, id_movement_type=mt1.id, id_movement_category=mc1.id, id_account=a1.id)
    m_client.create(m1, session)    
    m2 = Movement(id=uuid.uuid4(), date=datetime.datetime.now(), id_payment_method=pm2.id, id_movement_type=mt2.id, id_movement_category=mc2.id, id_account=a1.id)
    m_client.create(m2, session)

