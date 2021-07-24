from pydantic import BaseModel
from fastapi import Query
from schemas.genderEnum import GenderEnum

class Pasien(BaseModel):
    name: str = Query(..., min_length=3)
    gender: GenderEnum
    address: str = Query(..., min_length=3)
    religion: str = Query(..., min_length=3)
    profession: str = Query(..., min_length=3)
    nationality: str = Query(..., min_length=3)
    pic: str = Query(..., min_length=3)
    pic_phone: str = Query(..., min_length=5)
    note: str = Query(..., min_length=3)
