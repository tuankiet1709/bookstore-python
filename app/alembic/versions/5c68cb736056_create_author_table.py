"""create author table

Revision ID: 5c68cb736056
Revises: 
Create Date: 2023-12-04 16:12:49.334735

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from schemas.base_entity import Gender


# revision identifiers, used by Alembic.
revision: str = '5c68cb736056'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'authors',
        sa.Column('id', sa.String(36), nullable=False, primary_key=True),
        sa.Column('full_name', sa.String(16), nullable=False),
        sa.Column('gender', sa.Enum(Gender), nullable=False, default=Gender.NONE),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime)
    )


def downgrade() -> None:
    op.drop_table('authors')
