"""empty message

Revision ID: 5b33c7b4d1f1
Revises: c66b2d7f7d64
Create Date: 2021-07-19 10:06:48.848589

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5b33c7b4d1f1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('workOrders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customerId', sa.String(length=100), nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('startDate', sa.DateTime(), nullable=False),
    sa.Column('serviceId', sa.Integer(), nullable=False),
    sa.Column('employeeId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['employeeId'], ['employees.id'], ),
    sa.ForeignKeyConstraint(['serviceId'], ['services.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_workOrders_startDate'), 'workOrders', ['startDate'], unique=False)
    op.drop_table('workorders')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('workorders',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('serviceId', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('createdAt', mysql.DATETIME(), nullable=False),
    sa.Column('startDate', mysql.DATETIME(), nullable=False),
    sa.Column('customerId', mysql.VARCHAR(length=50), server_default=sa.text("''"), nullable=False),
    sa.Column('employeeId', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='MyISAM'
    )
    op.drop_index(op.f('ix_workOrders_startDate'), table_name='workOrders')
    op.drop_table('workOrders')
    # ### end Alembic commands ###
