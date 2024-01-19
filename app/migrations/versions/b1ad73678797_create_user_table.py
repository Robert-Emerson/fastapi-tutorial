"""create user table

Revision ID: b1ad73678797
Revises: 
Create Date: 2024-01-19 11:37:24.715271

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b1ad73678797'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

table_name = 'user'

def upgrade() -> None:
    op.create_table(
        table_name,
        sa.Column('id', sa.Unicode(32), primary_key=True),
        sa.Column('first_name', sa.Unicode(50)),
        sa.Column('birthday', sa.Date)
    )


def downgrade() -> None:
    op.drop_table(table_name)
