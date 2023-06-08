from sqlalchemy.orm import Session
from models.MtrCostCenterModel import MtrCostCenterModel
from schemas import MtrCostCenterSchema
from fastapi import HTTPException, status

def get_mtr_cost_centers_cruds(db:Session,offset:int=0, limit:int=100):
    return db.query(MtrCostCenterModel).order_by(MtrCostCenterModel.cost_center_id).offset(offset).limit(limit).all()

def get_mtr_cost_center_cruds(db:Session,get_id:int):
    return  db.query(MtrCostCenterModel).filter(MtrCostCenterModel.cost_center_id==get_id).first()

def post_mtr_cost_center(db: Session, cost_center: MtrCostCenterSchema.MtrCostCenterSchema):
    _cost_center = MtrCostCenterModel()
    _cost_center.cost_center_id = cost_center.cost_center_id
    _cost_center.cost_center_code = cost_center.cost_center_code
    _cost_center.cost_center_name = cost_center.cost_center_name

    db.add(_cost_center)
    db.commit()
    db.refresh(_cost_center)

    return _cost_center


def update_mtr_cost_center(db:Session,update_id:int,request:MtrCostCenterSchema.MtrUpdateCostCenterSchema):
    _cost_center  = get_mtr_cost_center_cruds(db, update_id)
    _cost_center.is_active = request.is_active
    _cost_center.cost_center_name = request.cost_center_name
    _cost_center.cost_center_code = request.cost_center_code
    db.commit()
    db.refresh(_cost_center)
    return _cost_center



def del_mtr_cost_center(db:Session,del_id:int):
    _cost_center = get_mtr_cost_center_cruds(db=db,get_id=del_id)
    db.delete(_cost_center)
    db.commit()
    return {
        "status_code":200,
        "msg_status":"deleted"
    }


