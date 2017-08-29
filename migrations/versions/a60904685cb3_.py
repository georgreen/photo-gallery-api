"""empty message

Revision ID: a60904685cb3
Revises: 8c44b20fa86f
Create Date: 2017-08-31 19:29:21.686608

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a60904685cb3'
down_revision = '8c44b20fa86f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pictures', sa.Column('day_time', sa.String(), nullable=True))
    op.drop_column('pictures', 'time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pictures', sa.Column('time', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('pictures', 'day_time')
    # ### end Alembic commands ###
