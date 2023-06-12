from sqlalchemy import String,Column,Float,Integer, Boolean, Numeric, text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from configs.database import Base,engine

class MtrProfitCenterBusinessCategory(Base):
    __tablename__ = "mtr_profit_center_business_category"
    is_active = Column(Boolean,nullable=False,default=True)
    profit_center_business_category_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    business_category_id = Column(Integer, ForeignKey("mtr_business_category.business_category_id"), nullable=False)
    profit = relationship("MtrProfitCenter", back_populates="business_category")
    business_category = relationship("MtrBusinessCategory", back_populates="profit")