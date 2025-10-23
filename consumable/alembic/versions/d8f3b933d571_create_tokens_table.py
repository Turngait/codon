"""create tokens table

Revision ID: d8f3b933d571
Revises: ec10dd7ff37c
Create Date: 2025-10-23 11:12:03.367369

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd8f3b933d571'
down_revision: Union[str, Sequence[str], None] = 'ec10dd7ff37c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tokens',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey("users.id")),
        sa.Column('token', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('active_til', sa.DateTime(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('tokens')
