from sqlalchemy.orm import Session
from models import MtrDeductionDetailModel

def get_mtr_deduction_detail_cruds(db:Session,offset:int=0, limit:int=100):
    return db.query(MtrDeductionDetailModel.MtrDeductionDetailModel).order_by(MtrDeductionDetailModel.MtrDeductionDetailModel.deduction_detail_id).offset(offset).limit(limit).all()

