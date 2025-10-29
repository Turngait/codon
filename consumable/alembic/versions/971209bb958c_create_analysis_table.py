"""create analysis table

Revision ID: 971209bb958c
Revises: c7399af5346b
Create Date: 2025-10-23 11:21:30.092525

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '971209bb958c'
down_revision: Union[str, Sequence[str], None] = 'c7399af5346b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'analysis',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(64), nullable=False),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('group_id', sa.Integer, sa.ForeignKey("analysis_groups.id")),
        sa.Column('clinic_id', sa.Integer, sa.ForeignKey("clinics.id")),
        sa.Column('date', sa.DateTime(), nullable=False),
        sa.Column('doctors', sa.String(64), nullable=True),
        sa.Column('equipment', sa.String(64), nullable=True),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('analysis')
