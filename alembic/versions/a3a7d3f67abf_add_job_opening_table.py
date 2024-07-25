"""add job opening table

Revision ID: a3a7d3f67abf
Revises: 624046b5b6b2
Create Date: 2024-07-17 16:34:34.376858

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3a7d3f67abf'
down_revision: Union[str, None] = '624046b5b6b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cart_items', 'price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=10, asdecimal=2),
               existing_nullable=False)
    op.alter_column('cart_items', 'total_price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=10, asdecimal=2),
               existing_nullable=False)
    op.alter_column('order', 'total_price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=10, asdecimal=2),
               existing_nullable=False)
    op.alter_column('payments', 'amount',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=10, asdecimal=3),
               existing_nullable=False)
    op.alter_column('products', 'product_price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=10, asdecimal=2),
               existing_nullable=False)
    op.alter_column('products', 'discount_percent',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=5, asdecimal=2),
               existing_nullable=False)
    op.alter_column('products', 'discount_price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=10, asdecimal=2),
               existing_nullable=False)
    op.alter_column('shipping_items', 'weight',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=10, asdecimal=2),
               existing_nullable=False)
    op.alter_column('shippings', 'shipping_cost',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=10, asdecimal=2),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('shippings', 'shipping_cost',
               existing_type=sa.Float(precision=10, asdecimal=2),
               type_=sa.REAL(),
               existing_nullable=False)
    op.alter_column('shipping_items', 'weight',
               existing_type=sa.Float(precision=10, asdecimal=2),
               type_=sa.REAL(),
               existing_nullable=False)
    op.alter_column('products', 'discount_price',
               existing_type=sa.Float(precision=10, asdecimal=2),
               type_=sa.REAL(),
               existing_nullable=False)
    op.alter_column('products', 'discount_percent',
               existing_type=sa.Float(precision=5, asdecimal=2),
               type_=sa.REAL(),
               existing_nullable=False)
    op.alter_column('products', 'product_price',
               existing_type=sa.Float(precision=10, asdecimal=2),
               type_=sa.REAL(),
               existing_nullable=False)
    op.alter_column('payments', 'amount',
               existing_type=sa.Float(precision=10, asdecimal=3),
               type_=sa.REAL(),
               existing_nullable=False)
    op.alter_column('order', 'total_price',
               existing_type=sa.Float(precision=10, asdecimal=2),
               type_=sa.REAL(),
               existing_nullable=False)
    op.alter_column('cart_items', 'total_price',
               existing_type=sa.Float(precision=10, asdecimal=2),
               type_=sa.REAL(),
               existing_nullable=False)
    op.alter_column('cart_items', 'price',
               existing_type=sa.Float(precision=10, asdecimal=2),
               type_=sa.REAL(),
               existing_nullable=False)
    # ### end Alembic commands ###
