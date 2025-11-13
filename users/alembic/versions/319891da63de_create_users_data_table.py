"""Create users data table

Revision ID: 319891da63de
Revises: 
Create Date: 2025-11-13 11:38:25.168155

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '319891da63de'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'data_of_users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('user_timezone', sa.String(50), nullable=True, default="+03:00"),
        sa.Column('status', sa.SmallInteger, nullable=False, default=1),
        sa.Column('isBanned', sa.Boolean(), nullable=True, default=False),
        sa.Column('biological_gender', sa.String(1), nullable=False),
        sa.Column('data_birth', sa.DateTime(), nullable=False),
        sa.Column('weight', sa.SmallInteger, nullable=False),
        sa.Column('height', sa.SmallInteger, nullable=False),
        sa.Column('lang_interface', sa.String(4), nullable=False, default="en"),
        sa.Column('theme_interface', sa.String(3), nullable=False, default="li"),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('data_of_users')
