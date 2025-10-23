"""create clinics_addreses table

Revision ID: ecefa339ecd5
Revises: 092066ed469f
Create Date: 2025-10-23 11:16:15.889300

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ecefa339ecd5'
down_revision: Union[str, Sequence[str], None] = '092066ed469f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'clinics_addresses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(64), nullable=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey("users.id")),
        sa.Column('address', sa.Text(), nullable=True),
        sa.Column('is_main', sa.Boolean(), nullable=True, default=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('clinics_addresses')
