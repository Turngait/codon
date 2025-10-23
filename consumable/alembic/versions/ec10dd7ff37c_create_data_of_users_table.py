"""create data_of_users table

Revision ID: ec10dd7ff37c
Revises: b9dc353f15f7
Create Date: 2025-10-23 10:58:17.364517

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec10dd7ff37c'
down_revision: Union[str, Sequence[str], None] = 'b9dc353f15f7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'data_of_users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey("users.id")),
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
