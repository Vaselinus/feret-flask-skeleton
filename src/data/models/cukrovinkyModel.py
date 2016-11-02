from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, Date

from ..database import db
from ..mixins import CRUDModel


class CukrovinkyDB(CRUDModel):
    __tablename__ = 'cukrovinky'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True)
    Druh = Column(String, nullable=False, index=True)
    Cena = Column(String, nullable=False, index=True)

