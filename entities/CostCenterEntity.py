from sqlalchemy import String,Column,Float,Integer, Boolean, Numeric, text
from sqlalchemy.orm import relationship
from configs.database import Base,engine

class MtrCostCenter(Base):
    __tablename__ = "mtr_cost_center"
    is_active = Column(Boolean,nullable=False,default=True)
    cost_center_id = Column(Integer,primary_key=True,nullable=False)
    cost_center_code = Column(String(10),nullable=True)
    cost_center_name = Column(String(100),nullable=True)
