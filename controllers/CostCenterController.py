from fastapi import APIRouter,Depends,HTTPException,status
from cruds import CostCenterCRUD
from exceptions.RequestException import ResponseException
from schemas import CostCenterSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from configs.database import get_db
from payloads import CommonResponse


router = APIRouter(tags=["Master Cost Center"],prefix="/api/general")
#bisa
@router.get("/get-master-cost-centers", status_code=200)
def get_master_cost_centers(db:Session=Depends(get_db)):
    master_cost_centers = CostCenterCRUD.get_mtr_cost_centers_cruds(db,0,100)
    if not get_master_cost_centers:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),master_cost_centers)

#bisa
@router.get("/get-master-cost-center/{cost_center_id}", status_code=status.HTTP_200_OK)
def get_master_cost_center(cost_center_id = None, db:Session=Depends(get_db)):
    master_cost_center = CostCenterCRUD.get_mtr_cost_center_cruds(db, cost_center_id)
    if not master_cost_center:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),master_cost_center)

#bisa
@router.post("/create-master-cost-center", status_code=201)
def post_master_cost_center(payload:CostCenterSchema.MtrCostCenterSchema,db:Session=Depends(get_db)):
    try:
        new_master_cost_center = CostCenterCRUD.post_mtr_cost_center(db, payload)
        db.add(new_master_cost_center)
        db.commit
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_master_cost_center)
    return CommonResponse.payload(ResponseException(201), new_master_cost_center)

#bisa
@router.put("/update-master-cost-center/{cost_center_id}",status_code=202)
def update_data(cost_center_id: int, payload:CostCenterSchema.UpdateCostCenterSchema, db:Session=Depends(get_db)):
    update_cost_center = CostCenterCRUD.update_mtr_cost_center(db,cost_center_id,payload)
    if not update_cost_center:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    
    db.refresh(update_cost_center)
    return CommonResponse.payload(ResponseException(200), update_cost_center)



#bisa
@router.delete("/delete-master-cost-center/{cost_center_id}", status_code=202)
def delete_master_cost_center(cost_center_id, db:Session=Depends(get_db)):
    erase_master_cost_center = CostCenterCRUD.del_mtr_cost_center(db,cost_center_id)
    if not erase_master_cost_center:
        db.rollback
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_master_cost_center)
