"""create packages table

Revision ID: 127f48f76f3e
Revises: 
Create Date: 2024-02-08 02:11:59.470167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '127f48f76f3e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('packages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sender', sa.String(length=255), nullable=True),
    sa.Column('recipient', sa.String(length=255), nullable=True),
    sa.Column('origin', sa.String(length=255), nullable=True),
    sa.Column('destination', sa.String(length=255), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('packages')
    # ### end Alembic commands ###
