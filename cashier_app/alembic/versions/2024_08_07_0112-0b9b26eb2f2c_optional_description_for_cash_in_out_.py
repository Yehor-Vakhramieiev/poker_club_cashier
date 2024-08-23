"""optional description for cash_in_out table

Revision ID: 0b9b26eb2f2c
Revises: 29d432ae8d05
Create Date: 2024-08-07 01:12:10.864685

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0b9b26eb2f2c"
down_revision: Union[str, None] = "29d432ae8d05"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "cash_in_outs", "description", existing_type=sa.VARCHAR(), nullable=True
    )


def downgrade() -> None:
    op.alter_column(
        "cash_in_outs", "description", existing_type=sa.VARCHAR(), nullable=False
    )
