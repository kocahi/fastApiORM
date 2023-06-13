from sqlalchemy import String,Column,Float,Integer, Boolean, Numeric, text
from sqlalchemy.orm import relationship
from configs.database import Base,engine

class MtrBrand(Base):
    __tablename__ = "mtr_brand"
    is_active = Column(Boolean,nullable=False,default=True)
    brand_id = Column(Integer, primary_key=True, nullable=False)
    supplier_id = Column(Integer, nullable=False)
    warehouse_id = Column(Integer, nullable=False)
    brand_code = Column(String(1), nullable=False)
    brand_name = Column(String(50), nullable=True)
    brand_abbreviation = Column(String(2), nullable=False)
    brand_must_withdrawl = Column(Boolean, nullable=True)
    brand_must_pdi = Column(Boolean, nullable=True)
    atpm_unit = Column(Boolean, nullable=True)
    atpm_workshop = Column(Boolean, nullable=True)
    atpm_sparepart = Column(Boolean, nullable=True)
    atpm_finance = Column(Boolean, nullable=True)
