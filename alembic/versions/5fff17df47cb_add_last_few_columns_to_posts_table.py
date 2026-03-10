"""add last few columns to posts table

Revision ID: 5fff17df47cb
Revises: 7d1c79de1cd3
Create Date: 2026-03-10 20:07:01.242890

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5fff17df47cb'
down_revision: Union[str, Sequence[str], None] = '7d1c79de1cd3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('publsihed',sa.Boolean(),server_default='TRUE'),)
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts','created_at')
    op.drop_column('posts','published')
    pass
