"""add foreign key to posts table

Revision ID: 7d1c79de1cd3
Revises: 2ff57ba1ddd9
Create Date: 2026-03-10 19:55:37.904828

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d1c79de1cd3'
down_revision: Union[str, Sequence[str], None] = '2ff57ba1ddd9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('posts_users_fk',
                          source_table="posts",referent_table="users",local_cols=['owner_id'],remote_cols=['id'],
                          ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk',table_name='posts')
    op.drop_column('posts','owner_id')
    pass
