from sqlalchemy.orm import Session
from models.MtrDeductionDetailModel import MtrDeductionDetailModel
from schemas import MtrDeductionDetailSchema
from fastapi import HTTPException, status

def get_mtr_deduction_details_cruds(db:Session,offset:int=0, limit:int=100):
    return db.query(MtrDeductionDetailModel).order_by(MtrDeductionDetailModel.deduction_detail_id).offset(offset).limit(limit).all()

def get_mtr_deduction_detail_cruds(db:Session,get_id:int):
    return  db.query(MtrDeductionDetailModel).filter(MtrDeductionDetailModel.deduction_detail_id==get_id).first()

def post_mtr_deduction_detail(db:Session,deduction_detail:MtrDeductionDetailSchema.MtrDeductionDetailSchema):
    _deduction_detail = MtrDeductionDetailModel()
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

def update_mtr_deduction_detail(db:Session,update_id:int,request:MtrDeductionDetailSchema.MtrUpdateDeductionDetailSchema):
    deduction_detail = db.query(MtrDeductionDetailModel).filter(MtrDeductionDetailModel.deduction_detail_id == update_id)
    if not deduction_detail.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Deduction detal with id {update_id} not found")
    deduction_detail.update({
        MtrDeductionDetailModel.is_active: request.is_active,
        MtrDeductionDetailModel.deduction_code: request.deduction_code,
        MtrDeductionDetailModel.deduction_level: request.deduction_level,
        MtrDeductionDetailModel.deduction_percent: request.deduction_percent,
        MtrDeductionDetailModel.limit_days: request.limit_days
    })
def update_mtr_deduction_detail(db:Session,update_id:int,deduction_detail:MtrDeductionDetailSchema.MtrDeductionDetailSchema):
    _deduction_detail = get_mtr_deduction_detail_cruds(db,update_id)
    _deduction_detail.deduction_code = deduction_detail.deduction_code
    _deduction_detail.deduction_level = deduction_detail.deduction_level
    _deduction_detail.deduction_percent = deduction_detail.deduction_percent
    _deduction_detail.limit_days = deduction_detail.deduction_level
    db.commit()
    return "ok"

    # _deduction_detail = get_mtr_deduction_detail_cruds(db,update_id)
    # _deduction_detail.deduction_code = deduction_detail.deduction_code
    # _deduction_detail.deduction_level = deduction_detail.deduction_level
    # _deduction_detail.deduction_percent = deduction_detail.deduction_percent
    # _deduction_detail.limit_days = deduction_detail.deduction_level
    # db.commit()
    # db.refresh(_deduction_detail)
    # return _deduction_detail