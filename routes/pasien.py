from config.db import con
from typing import Optional
from fastapi import APIRouter
from models.pasien import pasiens
from schemas.pasien import Pasien

pasien = APIRouter()


@pasien.get("/pasien")
def read_pasien():
    return con.execute(pasiens.select()).fetchall()


@pasien.get("/pasien/{pasien_id}")
def find_pasien(pasien_id: int):
    return con.execute(pasiens.select().where(pasiens.c.id == pasien_id)).fetchall()


@pasien.post("/pasien")
def create_pasien(pasien: Pasien):
    con.execute(pasiens.insert().values(
        name = pasien.name,
        gender = pasien.gender,
        address = pasien.address,
        religion = pasien.religion,
        profession = pasien.profession,
        nationality = pasien.nationality,
        pic = pasien.pic,
        pic_phone = pasien.pic_phone,
        note = pasien.note,
    ))
    return {"message": "Pasien Create Successful"}


@pasien.put("/pasien/{pasien_id}")
def update_pasien(pasien_id: int, pasien: Pasien):
    con.execute(pasiens.update().values(
        name = pasien.name,
        gender = pasien.gender,
        address = pasien.address,
        religion = pasien.religion,
        profession = pasien.profession,
        nationality = pasien.nationality,
        pic = pasien.pic,
        pic_phone = pasien.pic_phone,
        note = pasien.note,
    ).where(pasiens.c.id == pasien_id))
    return {"message": "Pasien Update Successful"}


@pasien.delete("/pasien/{pasien_id}")
def delete_pasien(pasien_id: int):
    con.execute(pasiens.delete().where(pasiens.c.id == pasien_id))
    return {"message": "Pasien Delete Successful"}
