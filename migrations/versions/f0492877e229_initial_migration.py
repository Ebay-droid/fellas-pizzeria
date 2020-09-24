"""initial migration

Revision ID: f0492877e229
Revises: 
Create Date: 2020-09-24 17:00:36.543364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0492877e229'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pizzas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('size', sa.String(length=255), nullable=True),
    sa.Column('price', sa.String(length=255), nullable=True),
    sa.Column('crust', sa.String(length=255), nullable=True),
    sa.Column('toppings', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pizzas')
    # ### end Alembic commands ###