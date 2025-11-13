"""Create ips table

Revision ID: 3e6efdebef7c
Revises: 85ff549e8348
Create Date: 2025-11-13 11:42:32.615658

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e6efdebef7c'
down_revision: Union[str, Sequence[str], None] = '85ff549e8348'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'ips',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('ip_4', sa.String(32), nullable=False),
        sa.Column('ip_6', sa.String(64), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
    )

def downgrade() -> None:
    op.drop_table('ips')
