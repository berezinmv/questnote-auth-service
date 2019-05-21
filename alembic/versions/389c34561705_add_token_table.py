"""add_token_table

Revision ID: 389c34561705
Revises: ce16a4346c17
Create Date: 2019-05-21 19:03:42.370188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '389c34561705'
down_revision = 'ce16a4346c17'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'token',
        sa.Column('token', sa.String(50), primary_key=True),
        sa.Column('client_id', sa.Integer, sa.ForeignKey('client.client_id'), nullable=False),
        sa.Column('expired_at', sa.DateTime, nullable=False)
    )
    pass


def downgrade():
    op.drop_table('token')
    pass
