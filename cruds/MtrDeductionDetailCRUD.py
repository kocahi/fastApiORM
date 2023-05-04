from sqlalchemy.orm import Session
from models import MtrDeductionDetailModel
from schemas import MtrDeductionDetailSchema

def get_mtr_deduction_details_cruds(db:Session,offset:int=0, limit:int=100):
    return db.query(MtrDeductionDetailModel.MtrDeductionDetailModel).order_by(MtrDeductionDetailModel.MtrDeductionDetailModel.deduction_detail_id).offset(offset).limit(limit).all()

def get_mtr_deduction_detail_cruds(db:Session,get_id:int):
    return  db.query(MtrDeductionDetailModel.MtrDeductionDetailModel).filter(MtrDeductionDetailModel.MtrDeductionDetailModel.deduction_detail_id==get_id).first()

def post_mtr_deduction_detail(db:Session,deduction_detail:MtrDeductionDetailSchema.MtrDeductionDetailSchema):
    _deduction_detail = MtrDeductionDetailModel.MtrDeductionDetailModel()
    _deduction_detail.deduction_detail_id = deduction_detail.deduction_detail_id
    _deduction_detail.deduction_code = deduction_detail.deduction_code
    _deduction_detail.deduction_level = deduction_detail.deduction_level
    _deduction_detail.deduction_percent = deduction_detail.deduction_percent
    _deduction_detail.limit_days = deduction_detail.deduction_level
    db.add(_deduction_detail)
    db.commit()
    db.refresh(_deduction_detail)
    print(_deduction_detail)
    return _deduction_detail

def del_mtr_deduction_detail(db:Session,del_id:int):
    _deduction_detail = get_mtr_deduction_detail_cruds(db=db,get_id=del_id)
    db.delete(_deduction_detail)
    db.commit()
    return {
        "status_code":200,
        "msg_status":"deleted"
    }

def update_mtr_deduction_detail(db:Session,update_id:int,deduction_detail:MtrDeductionDetailSchema.MtrDeductionDetailSchema):
    _deduction_detail = get_mtr_deduction_detail_cruds(db,update_id)
    _deduction_detail = MtrDeductionDetailModel.MtrDeductionDetailModel()
    _deduction_detail.deduction_detail_id = deduction_detail.deduction_detail_id
    _deduction_detail.deduction_code = deduction_detail.deduction_code
    _deduction_detail.deduction_level = deduction_detail.deduction_level
    _deduction_detail.deduction_percent = deduction_detail.deduction_percent
    _deduction_detail.limit_days = deduction_detail.deduction_level
    db.commit()
    db.refresh(_deduction_detail)
    return _deduction_detail