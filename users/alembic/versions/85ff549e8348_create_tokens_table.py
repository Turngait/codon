"""Create tokens table

Revision ID: 85ff549e8348
Revises: 319891da63de
Create Date: 2025-11-13 11:40:15.012767

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '85ff549e8348'
down_revision: Union[str, Sequence[str], None] = '319891da63de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tokens',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('token', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('active_til', sa.DateTime(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('tokens')
