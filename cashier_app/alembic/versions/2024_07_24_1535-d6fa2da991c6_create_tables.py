"""create tables

Revision ID: d6fa2da991c6
Revises: 
Create Date: 2024-07-24 15:35:01.819445

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "d6fa2da991c6"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "cash_register",
        sa.Column("date", sa.DateTime(), nullable=False),
        sa.Column("amount", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_cash_register_id"), "cash_register", ["id"], unique=False)
    op.create_table(
        "chips_quantity",
        sa.Column("one", sa.Integer(), nullable=False),
        sa.Column("five", sa.Integer(), nullable=False),
        sa.Column("twenty_five", sa.Integer(), nullable=False),
        sa.Column("hundred", sa.Integer(), nullable=False),
        sa.Column("five_hundred", sa.Integer(), nullable=False),
        sa.Column("thousand", sa.Integer(), nullable=False),
        sa.Column("five_thousand", sa.Integer(), nullable=False),
        sa.Column("twenty_five_thousand", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_chips_quantity_id"), "chips_quantity", ["id"], unique=False
    )
    op.create_table(
        "expenses",
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("amount", sa.Float(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_expenses_id"), "expenses", ["id"], unique=False)
    op.create_table(
        "game_sessions",
        sa.Column("started_at", sa.DateTime(), nullable=False),
        sa.Column("finished_at", sa.DateTime(), nullable=True),
        sa.Column("rake", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_game_sessions_id"), "game_sessions", ["id"], unique=False)
    op.create_table(
        "players",
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("second_name", sa.String(), nullable=False),
        sa.Column("nickname", sa.String(), nullable=True),
        sa.Column("birth_date", sa.DateTime(), nullable=True),
        sa.Column("phone_number", sa.String(), nullable=True),
        sa.Column("club_card_number", sa.String(), nullable=False),
        sa.Column("current_credit_deposit", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("club_card_number"),
    )
    op.create_index(op.f("ix_players_id"), "players", ["id"], unique=False)
    op.create_table(
        "credits_deposits",
        sa.Column("player_id", sa.Integer(), nullable=False),
        sa.Column("given_at", sa.DateTime(), nullable=False),
        sa.Column(
            "operation_type",
            sa.Enum("credit", "deposit", name="operationtype"),
            nullable=False,
        ),
        sa.Column("amount", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["player_id"],
            ["players.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_credits_deposits_id"), "credits_deposits", ["id"], unique=False
    )
    op.create_table(
        "player_sessions",
        sa.Column("player_id", sa.Integer(), nullable=False),
        sa.Column("started_at", sa.DateTime(), nullable=True),
        sa.Column("finished_at", sa.DateTime(), nullable=True),
        sa.Column("win_loss_amount", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["player_id"],
            ["players.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_player_sessions_id"), "player_sessions", ["id"], unique=False
    )
    op.create_table(
        "table_sessions",
        sa.Column("game_session_id", sa.Integer(), nullable=False),
        sa.Column("table_number", sa.Integer(), nullable=False),
        sa.Column("game_type", sa.String(), nullable=False),
        sa.Column("started_at", sa.DateTime(), nullable=False),
        sa.Column("finished_at", sa.DateTime(), nullable=True),
        sa.Column("rake", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["game_session_id"],
            ["game_sessions.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_table_sessions_id"), "table_sessions", ["id"], unique=False
    )
    op.create_table(
        "cash_in_outs",
        sa.Column("player_session_id", sa.Integer(), nullable=False),
        sa.Column(
            "type", sa.Enum("cash_in", "cash_out", name="operationtype"), nullable=False
        ),
        sa.Column("amount", sa.Integer(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["player_session_id"],
            ["player_sessions.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_cash_in_outs_id"), "cash_in_outs", ["id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_cash_in_outs_id"), table_name="cash_in_outs")
    op.drop_table("cash_in_outs")
    op.drop_index(op.f("ix_table_sessions_id"), table_name="table_sessions")
    op.drop_table("table_sessions")
    op.drop_index(op.f("ix_player_sessions_id"), table_name="player_sessions")
    op.drop_table("player_sessions")
    op.drop_index(op.f("ix_credits_deposits_id"), table_name="credits_deposits")
    op.drop_table("credits_deposits")
    op.drop_index(op.f("ix_players_id"), table_name="players")
    op.drop_table("players")
    op.drop_index(op.f("ix_game_sessions_id"), table_name="game_sessions")
    op.drop_table("game_sessions")
    op.drop_index(op.f("ix_expenses_id"), table_name="expenses")
    op.drop_table("expenses")
    op.drop_index(op.f("ix_chips_quantity_id"), table_name="chips_quantity")
    op.drop_table("chips_quantity")
    op.drop_index(op.f("ix_cash_register_id"), table_name="cash_register")
    op.drop_table("cash_register")
