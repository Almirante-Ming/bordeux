"""first

Revision ID: b0e186e8d52d
Revises: 
Create Date: 2025-01-17 07:45:38.253410

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b0e186e8d52d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'authors',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(50), nullable=False),
        sa.Column('nickname', sa.String(50), nullable=False),
        sa.Column('active', sa.Boolean, default=True)
    )
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('content', sa.String(50), nullable=False),
        sa.Column('author_id', sa.Integer, sa.ForeignKey('authors.id'), nullable=False),
        sa.Column('date', sa.DateTime, nullable=False),
        sa.column('priority', sa.String(50))
    )
def downgrade() -> None:
    op.drop_table('authors')
    op.drop_table('posts')
