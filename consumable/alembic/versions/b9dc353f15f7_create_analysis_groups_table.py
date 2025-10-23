"""create analysis groups table

Revision ID: b9dc353f15f7
Revises: 7cf1af5dd2bd
Create Date: 2025-10-22 13:23:47.756337

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9dc353f15f7'
down_revision: Union[str, Sequence[str], None] = '7cf1af5dd2bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'analysis_groups',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(64), nullable=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey("users.id")),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('analysis_groups')
