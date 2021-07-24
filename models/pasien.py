from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Enum, Unicode
from config.db import meta

pasiens = table('pasien',
    column('id', Integer),
    column('name', String(50)),
    column('gender', Enum('L', 'P')),
    column('address', Unicode(255)),
    column('religion', String(50)),
    column('profession', String(50)),
    column('nationality', String(50)),
    column('pic', String(50)),
    column('pic_phone', String(50)),
    column('note', Unicode(255)),
)
