"""first migrations

Revision ID: 3ffbca7b37d5
Revises: 
Create Date: 2025-10-16 11:42:40.191856

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3ffbca7b37d5'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(64), nullable=False),
        sa.Column('is_email_confirm', sa.Boolean(), nullable=True),
        sa.Column('password', sa.Text(), nullable=False),
        sa.Column('paper', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('analysis_groups')
