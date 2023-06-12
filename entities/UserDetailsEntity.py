from sqlalchemy import String,Column,Float,Integer, Boolean, Numeric, text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from configs.database import Base,engine

class TableName(Base):
    __tablename__ = 'mtr_user_details'
    is_active = Column(Boolean, default=True, nullable=False)
    user_employee_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    employee_name = Column(String(35), nullable=False)
    employee_nickname = Column(String(30), nullable=True)
    id_type = Column(String(10), nullable=True)
    id_no = Column(String(35), nullable=True)
    company_id = Column(Integer, nullable=False)
    job_title_id = Column(Integer, nullable=False)
    job_position_id = Column(Integer, nullable=False)
    division_id = Column(Integer, nullable=False)
    cost_center_id = Column(Integer, nullable=False)
    profit_center_id = Column(Integer, nullable=False)
    user_bank_account_id = Column(Integer, nullable=False)
    address_id = Column(Integer, nullable=False)
    office_phone_no = Column(String(30), nullable=True)
    home_phone_no = Column(String(30), nullable=True)
    mobile_phone = Column(String(30), nullable=True)
    email_address = Column(String(100), nullable=True)
    start_date = Column(DateTime, nullable=True)
    termination_date = Column(DateTime, nullable=True)
    gender = Column(String(1), nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    city_of_birth = Column(Integer, nullable=False)
    marital_status = Column(String(1), nullable=False)
    no_of_children = Column(Integer, nullable=True)
    citizenship = Column(String(35), nullable=True)
    last_education = Column(String(50), nullable=True)
    last_employment = Column(String(50), nullable=True)
    factor_x = Column(Numeric(20), nullable=True)
    skill_level_id = Column(Integer, nullable=False)
