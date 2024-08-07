"""initial migrationd

Revision ID: b81dffe5cd49
Revises: 
Create Date: 2024-03-27 18:23:38.832181

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'b81dffe5cd49'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_email', table_name='user')
    op.drop_table('user')
    op.add_column('path', sa.Column('path_skybox_image', sa.String(length=255), nullable=True))
    op.add_column('path', sa.Column('path_env_image', sa.String(length=255), nullable=True))
    op.create_unique_constraint(None, 'path', ['path_env_image'])
    op.create_unique_constraint(None, 'path', ['path_skybox_image'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'path', type_='unique')
    op.drop_constraint(None, 'path', type_='unique')
    op.drop_column('path', 'path_env_image')
    op.drop_column('path', 'path_skybox_image')
    op.create_table('user',
    sa.Column('email', mysql.VARCHAR(length=320), nullable=False),
    sa.Column('hashed_password', mysql.VARCHAR(length=1024), nullable=False),
    sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.Column('is_superuser', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.Column('is_verified', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.Column('id', mysql.CHAR(length=36), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_user_email', 'user', ['email'], unique=True)
    # ### end Alembic commands ###
