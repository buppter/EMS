"""empty message

Revision ID: e17af90a5441
Revises: 
Create Date: 2020-02-07 17:32:29.976841

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e17af90a5441'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('db_employee', sa.Column('_gender', sa.Integer(), nullable=True, comment='性别'))
    op.drop_column('db_employee', 'gender')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('db_employee', sa.Column('gender', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='性别'))
    op.drop_column('db_employee', '_gender')
    # ### end Alembic commands ###
