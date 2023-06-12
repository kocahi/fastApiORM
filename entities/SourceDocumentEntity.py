from sqlalchemy import String,Column,Float,Integer, Boolean, Numeric, text
from sqlalchemy.orm import relationship
from configs.database import Base


class MtrSourceDocument(Base):
    __tablename__ = 'mtr_source_document'

    mtr_source_document_id = Column(Integer, primary_key=True, nullable=False)
    source_document_type_id = Column(Integer, nullable=False)
    brand_id = Column(Integer, nullable=False) #fk
    profit_center_id = Column(Integer, nullable=False) #fk
    transaction_type_id = Column(Integer, nullable=False) #fk
    bank_company_id = Column(Integer, nullable=False) #fk
    reset_frequency_id = Column(Integer, nullable=False) #fk
    source_document_name = Column(String(128), nullable=False)
    source_document_format = Column(String(50), nullable=False)
    source_document_reference = Column(Boolean, nullable=False)
    signature_employee_1 = Column(Integer, nullable=False) #fk
    signature_title_1 = Column(String(50), nullable=False)
    signature_employee_2 = Column(Integer, nullable=False) #fk
    signature_title_2 = Column(String(50), nullable=False)
    signature_employee_3 = Column(Integer, nullable=False) #fk
    signature_title_3 = Column(String(50), nullable=False)
    signature_employee_4 = Column(Integer, nullable=False)
    signature_title_4 = Column(String(50), nullable=False)
    source_document_source_doc_prefix = Column(String(128), nullable=True)
    source_document_brand_prefix = Column(String(128), nullable=True)
    source_document_profit_cost_center_prefix = Column(String(128), nullable=True)
    source_document_transaction_type_prefix = Column(String(128), nullable=True)
    source_document_bank_acc_prefix = Column(String(128), nullable=True)
    source_document_auto_number = Column(Boolean, nullable=False)



