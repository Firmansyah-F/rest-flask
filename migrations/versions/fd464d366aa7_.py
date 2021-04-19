"""empty message

Revision ID: fd464d366aa7
Revises: 
Create Date: 2021-04-16 10:25:59.341589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd464d366aa7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('level', sa.Enum('admin', 'supervisor', 'planner', 'worker', name='role_enum'), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('task',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=False),
    sa.Column('duedate', sa.DateTime(), nullable=False),
    sa.Column('status', sa.Enum('approve', 'submit', 'reject', name='status_enum'), nullable=True),
    sa.Column('attachment', sa.String(length=250), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('coment',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['task_id'], ['task.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('coment')
    op.drop_table('task')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
