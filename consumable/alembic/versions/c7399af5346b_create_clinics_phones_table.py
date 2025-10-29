"""create clinics_phones table

Revision ID: c7399af5346b
Revises: ecefa339ecd5
Create Date: 2025-10-23 11:20:11.330273

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c7399af5346b'
down_revision: Union[str, Sequence[str], None] = 'ecefa339ecd5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'clinics_phones',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(64), nullable=False),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('phone_number', sa.Text(), nullable=True),
        sa.Column('is_main', sa.Boolean(), nullable=True, default=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('clinics_phones')
