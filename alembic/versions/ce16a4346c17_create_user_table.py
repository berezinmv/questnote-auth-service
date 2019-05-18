"""create_user_table

Revision ID: ce16a4346c17
Revises: 
Create Date: 2019-05-16 21:38:01.906260

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ce16a4346c17'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('user_id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('email', sa.String(255), unique=True),
        sa.Column('password', sa.String(128)),
        sa.Column('name', sa.String(200), nullable=False),
    )
    pass


def downgrade():
    pass
