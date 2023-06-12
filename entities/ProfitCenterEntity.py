from sqlalchemy import String,Column,Float,Integer, Boolean, Numeric, text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from configs.database import Base,engine

class MtrProfitCenter(Base):
    __tablename__ = "mtr_profit_center"
    is_active = Column(Boolean,nullable=False,default=True)
    profit_center_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    profit_center_code = Column(String(10), nullable=False, default="")
    profit_center_name = Column(String(100), nullable=True, default="")
    profit_center_business_category_id = Column(Integer, ForeignKey("mtr_profit_center_business_category.profit_center_business_category_id"), nullable=False)
    business_category = relationship("MtrProfitCenterBusinessCategory", back_populates="profit")