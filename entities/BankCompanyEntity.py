from sqlalchemy import String,Column,Float,Integer, Boolean, Numeric, text
from sqlalchemy.orm import relationship
from configs.database import Base,engine


class TableName(Base):
    __tablename__ = 'mtr_bank_company'
    is_active = Column(Boolean,nullable=False,default=True)
    bank_company_id = Column(Integer, primary_key=True, nullable=False)
    company_id = Column(Integer, nullable=False)
    bank_company_code = Column(String(10), nullable=False)
    bank_account_type = Column(String(1), nullable=True)
    bank_company_description = Column(String(50), nullable=False)
    bank_id = Column(Integer, nullable=False)
    bank_branch_id = Column(Integer, nullable=False)
    bank_company_account_no = Column(String(50), nullable=False)
    bank_company_account_name = Column(String(60), nullable=False)
    account_type_id = Column(Integer, nullable=False)
    currency_id = Column(Integer, nullable=False)
    bank_company_receive = Column(Boolean, nullable=True)
    bank_company_disbursement = Column(Boolean, nullable=True)
    bank_company_balance_limit = Column(Float, nullable=False)
    bank_company_payment_limit = Column(Float, nullable=False)
    bank_company_allow_overdraft = Column(Boolean, nullable=True)
    brand_id = Column(Integer, nullable=False)
    profit_center_business_category_id = Column(Integer, nullable=False)
    cost_center_id = Column(Integer, nullable=False)
    daily_rpt_code = Column(String(50), nullable=True)
    vat_map = Column(String(3), nullable=True)
    qris_mpan = Column(String(35), nullable=True)
