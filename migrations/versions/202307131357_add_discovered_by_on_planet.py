"""Add discovered_by on planet

Revision ID: 505c1bbf1570
Revises: 76cd8afe1a19
Create Date: 2023-07-13 13:57:27.076922

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '505c1bbf1570'
down_revision = '76cd8afe1a19'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('locations', schema=None) as batch_op:
        batch_op.add_column(sa.Column('discovered_by', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_locations_discovered_by_players'), 'players', ['discovered_by'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('locations', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_locations_discovered_by_players'), type_='foreignkey')
        batch_op.drop_column('discovered_by')

    # ### end Alembic commands ###