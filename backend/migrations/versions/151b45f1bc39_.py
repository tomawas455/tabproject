"""empty message

Revision ID: 151b45f1bc39
Revises: 7f7f4be2077b
Create Date: 2022-04-16 12:58:06.671821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '151b45f1bc39'
down_revision = '7f7f4be2077b'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """INSERT INTO cities
            (city) VALUES
            ('Warszawa'),
            ('Kraków'),
            ('Wrocław'),
            ('Katowice'),
            ('Gliwice'),
            ('Białystok'),
            ('Chorzów')
        """
    )
    op.execute(
        """ INSERT INTO places
        (address, city_id) VALUES
        ('ul. Chmielna 21', (SELECT id FROM cities WHERE city='Warszawa')),
        ('ul. Marszałowska 8', (SELECT id FROM cities WHERE city='Warszawa')),
        ('ul. Szczepańska 12', (SELECT id FROM cities WHERE city='Kraków')),
        ('ul. Świętego Jana 6', (SELECT id FROM cities WHERE city='Kraków')),
        ('ul. Grodzka 536', (SELECT id FROM cities WHERE city='Kraków')),
        ('ul. Śląska 2', (SELECT id FROM cities WHERE city='Wrocław')),
        ('ul. Mariacka 21', (SELECT id FROM cities WHERE city='Katowice')),
        ('ul. Dworcowa 37', (SELECT id FROM cities WHERE city='Katowice')),
        ('ul. Akademicka 16', (SELECT id FROM cities WHERE city='Gliwice')),
        ('ul. Akademicka 8a', (SELECT id FROM cities WHERE city='Gliwice')),
        ('ul. Łóżycka 6', (SELECT id FROM cities WHERE city='Gliwice')),
        ('ul. Szkolna 27', (SELECT id FROM cities WHERE city='Białystok')),
        ('ul. Cicha 6', (SELECT id FROM cities WHERE city='Chorzów'))
        """
    )
    op.execute(
        """ INSERT INTO tags
        (name) VALUES
        ('programowanie'),
        ('rozwoj osobisty'),
        ('edukacja'),
        ('fizyka'),
        ('c++'),
        ('python'),
        ('finanse')
        """
    )




def downgrade():
    op.execute("DELETE FROM cities")
    op.execute("DELETE FROM places")
    op.execute("DELETE FROM tags")
