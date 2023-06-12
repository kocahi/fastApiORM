from sqlalchemy import String,Column,Float,Integer, Boolean, Numeric, text
from sqlalchemy.orm import relationship
from configs.database import Base,engine


class MtrBusinessCategory(Base):
    __tablename__ = "mtr_business_category"
    is_active = Column(Boolean,nullable=False,default=True)
    business_category_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    business_category_code = Column(String(20), nullable=True, default="")
    business_category_name = Column(String(256), nullable=True, default="")
    profit = relationship("MtrProfitCenterBusinessCategory", back_populates="business_category")