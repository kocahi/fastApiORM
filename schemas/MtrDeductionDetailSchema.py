from typing import Optional

from pydantic import BaseModel

class MtrDeductionDetailSchema(BaseModel):
    is_active: Optional[bool] = None 
    deduction_detail_id: Optional[int] = None
    deduction_code: str
    deduction_level: int
    limit_days: int
    deduction_percent: float

    class Config:
        orm_mode = True

class GetMasterDeductionDetailsResponse(BaseModel):
    detail: str
    data: Optional[MtrDeductionDetailSchema]


class MtrUpdateDeductionDetailSchema(BaseModel):
    is_active: Optional[bool] = None 
    deduction_code: str
    deduction_level: int
    limit_days: int
    deduction_percent: float

    class Config:
        orm_mode = True
