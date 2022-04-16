"""empty message

Revision ID: 29ef7fb1d86b
Revises: 92f7de52c9b5
Create Date: 2022-03-27 12:55:13.942468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29ef7fb1d86b'
down_revision = '92f7de52c9b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courses',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.Unicode(length=100), nullable=False),
                    sa.Column('description', sa.UnicodeText(), nullable=False),
                    sa.Column('expense', sa.Numeric(
                        precision=50, scale=2), nullable=False),
                    sa.Column('author_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('courses')
    # ### end Alembic commands ###
