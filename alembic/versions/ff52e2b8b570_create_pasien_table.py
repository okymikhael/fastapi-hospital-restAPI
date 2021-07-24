"""create pasien table

Revision ID: ff52e2b8b570
Revises: 
Create Date: 2021-07-23 19:36:36.888570

"""
from alembic import op
from models.pasien import pasiens
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff52e2b8b570'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'pasien',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('gender', sa.Enum('L', 'P'), nullable=False),
        sa.Column('address', sa.Unicode(255), nullable=False),
        sa.Column('religion', sa.String(50), nullable=False),
        sa.Column('profession', sa.String(50), nullable=False),
        sa.Column('nationality', sa.String(50), nullable=False),
        sa.Column('pic', sa.String(50), nullable=False),
        sa.Column('pic_phone', sa.String(50), nullable=False),
        sa.Column('note', sa.Unicode(255), nullable=True),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.current_timestamp()),
    )
    
    # # Uncomment if you need mock data    
    # op.bulk_insert(pasiens,
    #     [
    #         {
    #         "name":"Burhan Indie",
    #         "gender": "L",
    #         "address": "JL. Jakarta 31B Malang",
    #         "religion": "Islam",
    #         "profession": "Buruh",
    #         "nationality": "WNI",
    #         "pic": "Marbun Slank",
    #         "pic_phone": "+6285604056893",
    #         "note": "Kecelakan sepeda motor dengan pembatas jalan"
    #         },
    #         {
    #         "name":"Ed Monaap",
    #         "gender": "L",
    #         "address": "Laluan Sri Palma 3216",
    #         "religion": "Islam",
    #         "profession": "Nelayan",
    #         "nationality": "WNA Malaysia",
    #         "pic": "Suyitno",
    #         "pic_phone": "+6285019235893",
    #         "note": "Sesak nafas dan kejang"
    #         },
    #         {
    #         "name":"Angel Paik",
    #         "gender": "P",
    #         "address": "Hillview Green, No. 73 Hume Ave",
    #         "religion": "Islam",
    #         "profession": "Model",
    #         "nationality": "WNA Singapore",
    #         "pic": "Srimulyani",
    #         "pic_phone": "+6285604092732",
    #         "note": "Pingsan"
    #         },
    #     ]
    # )



def downgrade():
    op.drop_table('pasien')

