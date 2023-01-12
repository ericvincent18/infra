"""create wine_reviews table

Revision ID: a86a3032df6a
Revises: 
Create Date: 2023-01-12 17:26:33.712788

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'initial migration'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'wine_reviews',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('points', sa.Integer),
        sa.Column('title', sa.String(255)),
        sa.Column('description', sa.String(255)),
        sa.Column('taster_name', sa.String(255)),
        sa.Column('taster_twitter_handle', sa.String(255)),
        sa.Column('price', sa.Integer),
        sa.Column('designation', sa.String(255)),
        sa.Column('variety', sa.String(255)),
        sa.Column('region_1', sa.String(255)),
        sa.Column('region_2', sa.String(255)),
        sa.Column('province', sa.String(255)),
        sa.Column('country', sa.String(255)),
        sa.Column('winery', sa.String(255))
    )


def downgrade() -> None:
    op.drop_table('wine_reviews')
