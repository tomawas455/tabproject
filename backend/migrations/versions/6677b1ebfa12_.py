"""empty message

Revision ID: 6677b1ebfa12
Revises: 29ef7fb1d86b
Create Date: 2022-03-30 16:45:35.684596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6677b1ebfa12'
down_revision = '29ef7fb1d86b'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """INSERT INTO roles
            (name) VALUES
            ('user'),
            ('worker'),
            ('administrator')
        """
    )
    password = "pbkdf2:sha256:260000$rMoTDlGpKGfHahrM$df5ebf49873a1a92c931c0bc9a5fdf6b6dbb9bb9bb39df1e6a77ae9075e4c979"
    op.execute(
        """INSERT INTO users
            (name, surname, email, role_id, password) VALUES
            ('admin', 'istrator', 'admin@istrat.or', (SELECT id FROM roles WHERE name='administrator'), '{0}'),
            ('worker', '1', 'worker1@worker.mail', (SELECT id FROM roles WHERE name='worker'), '{0}'),
            ('worker', '2', 'worker2@worker.mail', (SELECT id FROM roles WHERE name='worker'), '{0}'),
            ('worker', '3', 'worker3@worker.mail', (SELECT id FROM roles WHERE name='worker'), '{0}'),
            ('worker', '4', 'worker4@worker.mail', (SELECT id FROM roles WHERE name='worker'), '{0}'),
            ('worker', '5', 'worker5@worker.mail', (SELECT id FROM roles WHERE name='worker'), '{0}'),
            ('user', '1', 'user1@user.mail', (SELECT id FROM roles WHERE name='user'), '{0}'),
            ('user', '2', 'user2@user.mail', (SELECT id FROM roles WHERE name='user'), '{0}'),
            ('user', '3', 'user3@user.mail', (SELECT id FROM roles WHERE name='user'), '{0}'),
            ('user', '4', 'user4@user.mail', (SELECT id FROM roles WHERE name='user'), '{0}'),
            ('user', '5', 'user5@user.mail', (SELECT id FROM roles WHERE name='user'), '{0}'),
            ('user', '6', 'user6@user.mail', (SELECT id FROM roles WHERE name='user'), '{0}'),
            ('user', '7', 'user7@user.mail', (SELECT id FROM roles WHERE name='user'), '{0}'),
            ('user', '8', 'user8@user.mail', (SELECT id FROM roles WHERE name='user'), '{0}'),
            ('user', '9', 'user9@user.mail', (SELECT id FROM roles WHERE name='user'), '{0}'),
            ('user', '10', 'user10@user.mail', (SELECT id FROM roles WHERE name='user'), '{0}'),
            ('Krzysztof', 'Jaworek', 'krzysztof@jaworek.mail', (SELECT id FROM roles WHERE name='user'), '{0}')
        """.format(password)
    )


def downgrade():
    op.execute("DELETE FROM roles")
    op.execute("DELETE FROM users")
