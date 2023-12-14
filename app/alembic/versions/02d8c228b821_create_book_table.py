"""create book table

Revision ID: 02d8c228b821
Revises: 5c68cb736056
Create Date: 2023-12-05 09:34:57.554321

"""
from typing import Sequence, Union

from alembic import op
from schemas.base_entity import BookMode
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02d8c228b821'
down_revision: Union[str, None] = '5c68cb736056'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'books',
        sa.Column('id', sa.String(36), nullable=False, primary_key=True),
        sa.Column('title', sa.String(36), nullable=False),
        sa.Column('description', sa.String(255)),
        sa.Column('mode', sa.Enum(BookMode), nullable=False, default=BookMode.DRAFT),
        sa.Column('rating', sa.SmallInteger, default=0),
        sa.Column('author_id', sa.String(36), nullable=False),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime)
    )
    op.create_foreign_key('fk_book_author', 'books', 'authors', ['author_id'], ['id'])

def downgrade() -> None:
    op.drop_table('books')
