"""empty message

Revision ID: a8c680c9354e
Revises: a64048310d75
Create Date: 2021-01-01 22:43:04.545024

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a8c680c9354e'
down_revision = 'a64048310d75'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('address', sa.Column('default_address', sa.Boolean(), nullable=True))
    op.add_column('address', sa.Column('street', sa.String(length=100), nullable=False))
    op.drop_column('address', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('address', sa.Column('address', mysql.VARCHAR(length=150), nullable=False))
    op.drop_column('address', 'street')
    op.drop_column('address', 'default_address')
    # ### end Alembic commands ###