"""replace item SKU with product ID and add fabric type

Revision ID: 005
Revises: 004
"""
from alembic import op
import sqlalchemy as sa

revision = "005"
down_revision = "004"
branch_labels = None
depends_on = None


def upgrade() -> None:
    connection = op.get_bind()
    inspector = sa.inspect(connection)
    if "_alembic_tmp_items" in inspector.get_table_names():
        op.drop_table("_alembic_tmp_items")
    item_columns = {column["name"] for column in sa.inspect(connection).get_columns("items")}
    if "product_id" not in item_columns:
        op.add_column("items", sa.Column("product_id", sa.String(length=50), nullable=True))
    op.execute("UPDATE items SET product_id = sku")
    with op.batch_alter_table("items") as batch_op:
        batch_op.drop_index("ix_items_sku")
        batch_op.alter_column(
            "product_id",
            existing_type=sa.String(length=50),
            existing_nullable=True,
            nullable=False,
        )
        batch_op.drop_column("sku")
        batch_op.add_column(
            sa.Column(
                "fabric_type",
                sa.String(length=100),
                server_default="Unspecified",
                nullable=False,
            )
        )
        batch_op.create_index("ix_items_product_id", ["product_id"], unique=True)


def downgrade() -> None:
    op.add_column("items", sa.Column("sku", sa.String(length=50), nullable=True))
    op.execute("UPDATE items SET sku = product_id")
    with op.batch_alter_table("items") as batch_op:
        batch_op.drop_index("ix_items_product_id")
        batch_op.drop_column("fabric_type")
        batch_op.alter_column(
            "sku",
            existing_type=sa.String(length=50),
            existing_nullable=True,
            nullable=False,
        )
        batch_op.drop_column("product_id")
        batch_op.create_index("ix_items_sku", ["sku"], unique=True)