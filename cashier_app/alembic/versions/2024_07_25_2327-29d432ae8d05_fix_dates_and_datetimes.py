"""fix dates and datetimes

Revision ID: 29d432ae8d05
Revises: d6fa2da991c6
Create Date: 2024-07-25 23:27:44.017175

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '29d432ae8d05'
down_revision: Union[str, None] = 'd6fa2da991c6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('credits_deposits', 'given_at',
                    existing_type=postgresql.TIMESTAMP(),
                    type_=sa.DateTime(timezone=True),
                    existing_nullable=False)
    op.alter_column('game_sessions', 'started_at',
                    existing_type=postgresql.TIMESTAMP(),
                    type_=sa.DateTime(timezone=True),
                    existing_nullable=False)
    op.alter_column('game_sessions', 'finished_at',
                    existing_type=postgresql.TIMESTAMP(),
                    type_=sa.DateTime(timezone=True),
                    existing_nullable=True)
    op.alter_column('player_sessions', 'started_at',
                    existing_type=postgresql.TIMESTAMP(),
                    type_=sa.DateTime(timezone=True),
                    existing_nullable=True)
    op.alter_column('player_sessions', 'finished_at',
                    existing_type=postgresql.TIMESTAMP(),
                    type_=sa.DateTime(timezone=True),
                    existing_nullable=True)
    op.alter_column('players', 'birth_date',
                    existing_type=postgresql.TIMESTAMP(),
                    type_=sa.Date(),
                    existing_nullable=True)
    op.alter_column('table_sessions', 'started_at',
                    existing_type=postgresql.TIMESTAMP(),
                    type_=sa.DateTime(timezone=True),
                    existing_nullable=False)
    op.alter_column('table_sessions', 'finished_at',
                    existing_type=postgresql.TIMESTAMP(),
                    type_=sa.DateTime(timezone=True),
                    existing_nullable=True)


def downgrade() -> None:
    op.alter_column('table_sessions', 'finished_at',
                    existing_type=sa.DateTime(timezone=True),
                    type_=postgresql.TIMESTAMP(),
                    existing_nullable=True)
    op.alter_column('table_sessions', 'started_at',
                    existing_type=sa.DateTime(timezone=True),
                    type_=postgresql.TIMESTAMP(),
                    existing_nullable=False)
    op.alter_column('players', 'birth_date',
                    existing_type=sa.Date(),
                    type_=postgresql.TIMESTAMP(),
                    existing_nullable=True)
    op.alter_column('player_sessions', 'finished_at',
                    existing_type=sa.DateTime(timezone=True),
                    type_=postgresql.TIMESTAMP(),
                    existing_nullable=True)
    op.alter_column('player_sessions', 'started_at',
                    existing_type=sa.DateTime(timezone=True),
                    type_=postgresql.TIMESTAMP(),
                    existing_nullable=True)
    op.alter_column('game_sessions', 'finished_at',
                    existing_type=sa.DateTime(timezone=True),
                    type_=postgresql.TIMESTAMP(),
                    existing_nullable=True)
    op.alter_column('game_sessions', 'started_at',
                    existing_type=sa.DateTime(timezone=True),
                    type_=postgresql.TIMESTAMP(),
                    existing_nullable=False)
    op.alter_column('credits_deposits', 'given_at',
                    existing_type=sa.DateTime(timezone=True),
                    type_=postgresql.TIMESTAMP(),
                    existing_nullable=False)
