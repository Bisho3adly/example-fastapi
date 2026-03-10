"""add_content_column_to_posts_table

Revision ID: 45a268672605
Revises: f39b20a9a2eb
Create Date: 2026-03-10 19:05:54.003991

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45a268672605'
down_revision: Union[str, Sequence[str], None] = 'f39b20a9a2eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
