from sqlalchemy import String,Column,Float,Integer, Boolean, Numeric, text
from sqlalchemy.orm import relationship
from configs.database import Base,engine

class MtrDeductionDetailModel(Base):
    __tablename__ = "mtr_deduction_detail"
    is_active = Column(Boolean,nullable=False,default=True)
    deduction_detail_id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    deduction_code = Column(String(50),nullable=True,default="")
    deduction_level = Column(Integer,nullable=False,default=0)
    limit_days = Column(Integer,nullable=False,default=0)
    deduction_percent = Column(Numeric(5, 2), nullable=False, server_default=text('((0))'))
