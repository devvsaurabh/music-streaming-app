"""empty message

Revision ID: b020fcb03111
Revises: da1003bce0d7
Create Date: 2020-09-14 00:28:52.809329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b020fcb03111'
down_revision = 'da1003bce0d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('music_store', sa.Column('filename', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('music_store', 'filename')
    # ### end Alembic commands ###
