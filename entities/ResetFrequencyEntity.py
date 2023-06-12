from sqlalchemy import String,Column,Float,Integer, Boolean, Numeric, text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from configs.database import Base,engine


class TableName(Base):
    __tablename__ = 'mtr_reset_frequency'
    is_active = Column(Boolean, default=True, nullable=False)
    reset_frequency_id = Column(Integer, primary_key=True, nullable=False)
    reset_frequency_code = Column(String(20), nullable=False)
    reset_frequency_name = Column(String(256), nullable=True)