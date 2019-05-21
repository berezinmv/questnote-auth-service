"""create_client_table

Revision ID: ce16a4346c17
Revises: 
Create Date: 2019-05-16 21:38:01.906260

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'ce16a4346c17'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'client',
        sa.Column('client_id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('email', sa.String(255), unique=True),
        sa.Column('password_hash', sa.String(128), nullable=False),
        sa.Column('name', sa.String(200)),
    )
    pass


def downgrade():
    op.drop_table('client')
    pass
