"""add item price in INR

Revision ID: 006
Revises: 005
"""
from alembic import op
import sqlalchemy as sa

revision = "006"
down_revision = "005"
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table("items") as batch_op:
        batch_op.add_column(
            sa.Column(
                "price_inr",
                sa.Numeric(12, 2),
                server_default="0.00",
                nullable=False,
            )
        )


def downgrade() -> None:
    with op.batch_alter_table("items") as batch_op:
        batch_op.drop_column("price_inr")