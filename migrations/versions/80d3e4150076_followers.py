"""Followers

Revision ID: 80d3e4150076
Revises: c7fdbf23d39b
Create Date: 2022-01-27 14:29:56.558492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80d3e4150076'
down_revision = 'c7fdbf23d39b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###