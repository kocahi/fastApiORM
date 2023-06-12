from fastapi import APIRouter,Depends,HTTPException,status
from cruds import DeductionDetailCRUD
from exceptions.RequestException import ResponseException
from schemas import DeductionDetailSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from configs.database import get_db
from payloads import CommonResponse


router = APIRouter(tags=["Master Deduction Detail"],prefix="/api/general")
#bisa
@router.get("/get-master-deduction-details", status_code=200)
def get_master_deduction_details(db:Session=Depends(get_db)):
    master_deduction_details = DeductionDetailCRUD.get_mtr_deduction_details_cruds(db,0,100)
    if not get_master_deduction_details:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),master_deduction_details)

#bisa
@router.get("/get-master-deduction-detail/{deduction_detail_id}", status_code=status.HTTP_200_OK)
def get_master_deduction_details(deduction_detail_id = None, db:Session=Depends(get_db)):
    master_deduction_detail = DeductionDetailCRUD.get_mtr_deduction_detail_cruds(db, deduction_detail_id)
    if not master_deduction_detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),master_deduction_detail)

#bisa
@router.post("/create-master-deduction-detail", status_code=201)
def post_master_deduction_detail(payload:DeductionDetailSchema.MtrUpdateDeductionDetailSchema,db:Session=Depends(get_db)):
    try:
        new_master_deduction_detail = DeductionDetailCRUD.post_mtr_deduction_detail(db, payload)
        db.add(new_master_deduction_detail)
        db.commit
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_master_deduction_detail)
    return CommonResponse.payload(ResponseException(201), new_master_deduction_detail)


#bisa
@router.put("/update-master-deduction-detail/{deduction_detail_id}",status_code=202)
def update_data(deduction_detail_id: int, payload:DeductionDetailSchema.UpdateDeductionDetailSchema, db:Session=Depends(get_db)):
    update_master_deduction_detail = DeductionDetailCRUD.update_mtr_deduction_details(db,deduction_detail_id,payload)
    if not update_master_deduction_detail:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_master_deduction_detail)
    return CommonResponse.payload(ResponseException(200), update_master_deduction_detail)


#bisa
@router.delete("/delete-master-deduction-detail/{deduction_detail_id}", status_code=202)
def delete_master_deduction_detail(deduction_detail_id, db:Session=Depends(get_db)):
    erase_master_deduction_detail = DeductionDetailCRUD.del_mtr_deduction_detail(db,deduction_detail_id)
    if not erase_master_deduction_detail:
        db.rollback
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_master_deduction_detail)



