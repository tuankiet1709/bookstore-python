"""create user table

Revision ID: 5a1503d7885d
Revises: 02d8c228b821
Create Date: 2023-12-05 17:55:18.801813

"""
from datetime import datetime
from typing import Sequence, Union
import uuid

from alembic import op
from settings import ADMIN_DEFAULT_PASSWORD
from schemas.user import get_password_hash
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5a1503d7885d'
down_revision: Union[str, None] = '02d8c228b821'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    user_table = op.create_table(
        "users",
        sa.Column("id", sa.String(36), nullable=False, primary_key=True),
        sa.Column("email", sa.String(50), unique=True, nullable=True, index=True),
        sa.Column("username", sa.String(50), unique=True, index=True),
        sa.Column("first_name", sa.String(50)),
        sa.Column("last_name", sa.String(50)),
        sa.Column("password", sa.String(120)),
        sa.Column("is_active", sa.Boolean, default=True),
        sa.Column("is_admin", sa.Boolean, default=False),
        sa.Column("created_at", sa.DateTime),
        sa.Column("updated_at", sa.DateTime)
    )
    op.create_index("idx_usr_fst_lst_name", "users", ["first_name", "last_name"])
    # Update Book Table
    op.add_column("books", sa.Column("owner_id", sa.String(36), nullable=True))
    op.create_foreign_key("fk_book_owner", "books", "users", ["owner_id"],['id'])
    
    # Data seed for first user
    op.bulk_insert(user_table, [
        {
            "id": str(uuid.uuid4()),
            "email": "admin@sample.com", 
            "username": "fa_admin",
            "password": get_password_hash(ADMIN_DEFAULT_PASSWORD),
            "first_name": "FastApi",
            "last_name": "Admin",
            "is_active": True,
            "is_admin": True,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": str(uuid.uuid4()),
            "email": "user@sample.com", 
            "username": "fa_user",
            "password": get_password_hash(ADMIN_DEFAULT_PASSWORD),
            "first_name": "FastApi",
            "last_name": "User",
            "is_active": True,
            "is_admin": False,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
    ])

def downgrade() -> None:
    # Rollback foreign key
    op.drop_column("books", "owner_id")
    # Rollback foreign key
    op.drop_table("users")
