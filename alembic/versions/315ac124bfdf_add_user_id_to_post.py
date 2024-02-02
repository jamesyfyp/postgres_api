"""add_user_id_to_post

Revision ID: 315ac124bfdf
Revises: a7ddb3bdbe8d
Create Date: 2024-02-01 20:59:15.081578

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '315ac124bfdf'
down_revision: Union[str, None] = 'a7ddb3bdbe8d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('post_s', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('fk_post_user_id', 'post_s', 'users_s', ['user_id'], ['id'])
    pass


def downgrade() -> None:
    op.drop_constraint('fk_post_user_id', 'post_s', type_='foreignkey')
    op.drop_column('post_s', 'user_id')
    pass
