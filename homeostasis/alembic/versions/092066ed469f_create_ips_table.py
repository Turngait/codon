"""create ips table

Revision ID: 092066ed469f
Revises: d8f3b933d571
Create Date: 2025-10-23 11:13:48.002996

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '092066ed469f'
down_revision: Union[str, Sequence[str], None] = 'd8f3b933d571'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'ips',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey("users.id")),
        sa.Column('ip_4', sa.String(32), nullable=False),
        sa.Column('ip_6', sa.String(64), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
    )

def downgrade() -> None:
    op.drop_table('ips')
