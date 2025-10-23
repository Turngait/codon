"""create clinics table

Revision ID: 7cf1af5dd2bd
Revises: 3ffbca7b37d5
Create Date: 2025-10-22 13:08:07.308473

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7cf1af5dd2bd'
down_revision: Union[str, Sequence[str], None] = '3ffbca7b37d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'clinics',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(64), nullable=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey("users.id")),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('main_site', sa.String(64), nullable=True),
        sa.Column('law_info', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('clinics')
