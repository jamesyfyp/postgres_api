"""Create chunk_s table

Revision ID: 7cc0d0459239
Revises: 315ac124bfdf
Create Date: 2024-03-04 06:00:05.036962

"""
from typing import Sequence, Union
from alembic import op
from pgvector.sqlalchemy import Vector
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision: str = '7cc0d0459239'
down_revision: Union[str, None] = '315ac124bfdf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
     op.create_table(
        'chunk_s',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users_s.id'), nullable=False),
        sa.Column('post_id', sa.Integer(), sa.ForeignKey('post_s.id'), nullable=False),
        sa.Column('chunk_number', sa.Integer(), nullable=False),
        sa.Column('text_chunk', sa.Text(), nullable=False),
        sa.Column('vector', Vector(384), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    


def downgrade():
    op.drop_table('chunk_s')
