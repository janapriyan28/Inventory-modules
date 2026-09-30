"""create stock_in table

Revision ID: 003
Revises: 002
"""
import sqlalchemy as sa
from alembic import op

revision = "003"
down_revision = "002"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "stock_in",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("item_id", sa.Integer, sa.ForeignKey("items.id"), nullable=False),
        sa.Column("warehouse_id", sa.Integer, sa.ForeignKey("warehouses.id"), nullable=False),
        sa.Column("quantity", sa.Integer, nullable=False),
        sa.Column("reference", sa.String(100), nullable=True),
        sa.Column("remarks", sa.String(500), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_index("ix_stock_in_item_id", "stock_in", ["item_id"])
    op.create_index("ix_stock_in_warehouse_id", "stock_in", ["warehouse_id"])


def downgrade() -> None:
    op.drop_index("ix_stock_in_warehouse_id", table_name="stock_in")
    op.drop_index("ix_stock_in_item_id", table_name="stock_in")
    op.drop_table("stock_in")
