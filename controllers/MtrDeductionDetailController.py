from fastapi import APIRouter,Depends,HTTPException,status
from cruds import MtrDeductionDetailCRUD
from exceptions.RequestException import ResponseException
from schemas import MtrDeductionDetailSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from configs.database import get_db
from payloads import CommonResponse


router = APIRouter(tags=["Master Deduction Detail"],prefix="/api/general")

@router.get("/get-master-deduction-detail", status_code=200)
def get_master_deduction_detail(db:Session=Depends(get_db)):
    master_deduction_detail = MtrDeductionDetailCRUD.get_mtr_deduction_detail_cruds(db,0,100)
    if not master_deduction_detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),master_deduction_detail)



