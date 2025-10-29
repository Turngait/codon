"""create analysis_values table

Revision ID: ac431030dd3a
Revises: 971209bb958c
Create Date: 2025-10-23 11:23:47.252312

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac431030dd3a'
down_revision: Union[str, Sequence[str], None] = '971209bb958c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'analysis_values',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(64), nullable=False),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('analysis_id', sa.Integer, sa.ForeignKey("analysis.id")),
        sa.Column('volume', sa.String(64), nullable=False),
        sa.Column('normal', sa.String(64), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('analysis_values')
