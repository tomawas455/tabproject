"""empty message

Revision ID: d61ba88f5408
Revises: 151b45f1bc39
Create Date: 2022-04-17 14:32:59.614616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd61ba88f5408'
down_revision = '151b45f1bc39'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """ INSERT INTO courses
        (name, description, expense, author_id) VALUES
        ('Kurs C++', 'Wspaniały kurs C++', '12.2', (SELECT id FROM users WHERE email='admin@istrat.or')),
        ('Jazda samochodem', 'Naucz się jeździć samochodem', '2900', (SELECT id FROM users WHERE email='admin@istrat.or')),
        ('Jazda rowerem', 'Naucz się jeździć rowerem', '2899.99', (SELECT id FROM users WHERE email='worker1@worker.mail')),
        ('Bazy danych', 'Znajdź Jaworka', '0', (SELECT id FROM users WHERE email='krzysztof@jaworek.mail')),
        ('Taniec ekstremalny', 'Najlepszy kurs tańca na śląsku', '123.10', (SELECT id FROM users WHERE email='worker2@worker.mail')),
        ('Kurs czytania', 'Poznaj tajniki czytania książek i innych napisów', '9', (SELECT id FROM users WHERE email='worker1@worker.mail'))
        """
    )

    op.execute(
        """ INSERT INTO trainings
        (price, places_amount, free_places_amount, begin_date, end_date, enrolment_begin_date,
            enrolment_end_date, course_id, place_id, author_id, instructor_id) VALUES
        ('10', '20', '17', '2022-03-12 11:50:00', '2022-03-12 13:50:00', '2022-02-12 11:50:00',
            '2022-03-05 14:50:00', (SELECT id FROM courses WHERE name='Jazda samochodem'),
            (SELECT id FROM places WHERE address='ul. Marszałowska 8' and city_id=(SELECT id FROM cities WHERE city='Warszawa')),
            (SELECT id FROM users WHERE email='worker2@worker.mail'), (SELECT id FROM users WHERE email='worker1@worker.mail')),
        ('11.50', '100', '0', '2022-03-12 11:50:00', '2022-03-12 15:50:00', '2022-02-20 08:00:00',
            '2022-03-11 23:59:59', (SELECT id FROM courses WHERE name='Kurs czytania'),
            (SELECT id FROM places WHERE address='ul. Dworcowa 37' and city_id=(SELECT id FROM cities WHERE city='Katowice')),
            (SELECT id FROM users WHERE email='krzysztof@jaworek.mail'), (SELECT id FROM users WHERE email='admin@istrat.or')),
        ('99.99', '5', '1', '2022-11-05 07:45:00', '2022-11-08 15:50:00', '2022-10-01 08:00:00',
            '2022-10-31 23:59:59', (SELECT id FROM courses WHERE name='Bazy danych'),
            (SELECT id FROM places WHERE address='ul. Akademicka 16' and city_id=(SELECT id FROM cities WHERE city='Gliwice')),
            (SELECT id FROM users WHERE email='user2@user.mail'), (SELECT id FROM users WHERE email='krzysztof@jaworek.mail')),
        ('5.25', '1000', '1000', '2022-10-30 14:45:00', '2022-11-04 15:50:00', '2021-11-01 12:00:00',
            '2022-09-30 20:00:00', (SELECT id FROM courses WHERE name='Kurs C++'),
            (SELECT id FROM places WHERE address='ul. Akademicka 16' and city_id=(SELECT id FROM cities WHERE city='Gliwice')),
            (SELECT id FROM users WHERE email='user2@user.mail'), (SELECT id FROM users WHERE email='user2@user.mail')),
        ('11.50', '100', '0', '2022-04-15 11:50:00', '2022-04-15 15:50:00', '2022-03-23 08:00:00',
            '2022-04-14 23:59:59', (SELECT id FROM courses WHERE name='Kurs czytania'),
            (SELECT id FROM places WHERE address='ul. Cicha 6' and city_id=(SELECT id FROM cities WHERE city='Chorzów')),
            (SELECT id FROM users WHERE email='krzysztof@jaworek.mail'), (SELECT id FROM users WHERE email='worker1@worker.mail'))
        """
    )


    op.execute(
        """ INSERT INTO participations
        (training_id, user_id, passed) VALUES
        ('1', (SELECT id FROM users WHERE email='user2@user.mail'), 'yes'),
        ('1', (SELECT id FROM users WHERE email='user1@user.mail'), 'no'),
        ('2', (SELECT id FROM users WHERE email='worker2@worker.mail'), 'yes'),
        ('3', (SELECT id FROM users WHERE email='worker1@worker.mail'), NULL),
        ('4', (SELECT id FROM users WHERE email='user1@user.mail'), NULL),
        ('5', (SELECT id FROM users WHERE email='admin@istrat.or'), 'no'),
        ('5', (SELECT id FROM users WHERE email='krzysztof@jaworek.mail'), 'yes')
        """
    )

    op.execute(
        """ INSERT INTO comments
        (text, creation_time, rate, author_id, course_id) VALUES
        ('Genialny kurs. \nPolecam.', '2022-01-30 14:45:00', '5',
            (SELECT id FROM users WHERE email='user2@user.mail'),
            (SELECT id FROM courses WHERE name='Kurs czytania')),
        ('Zawsze chciałem jeździć rowerem. \nTeraz wiem jak!', '2022-10-30 14:45:00', '3',
            (SELECT id FROM users WHERE email='user1@user.mail'),
            (SELECT id FROM courses WHERE name='Jazda rowerem')),
        ('Wskaźniki brrrrrr.', '2022-03-30 17:15:34', '2',
            (SELECT id FROM users WHERE email='user2@user.mail'),
            (SELECT id FROM courses WHERE name='Kurs C++')),
        ('Rowery nie miały działających hamulców!', '2021-11-13 01:37:12', '1',
            (SELECT id FROM users WHERE email='user1@user.mail'),
            (SELECT id FROM courses WHERE name='Jazda rowerem')),
        ('Kim jest ten Jaworek?', '2022-01-02 06:56:57', '3',
            (SELECT id FROM users WHERE email='krzysztof@jaworek.mail'),
            (SELECT id FROM courses WHERE name='Bazy danych'))
        """
    )

    op.execute(
        """ INSERT INTO course_tags
        (course_id, tag_id) VALUES
        ((SELECT id FROM courses WHERE name='Jazda rowerem'), 
            (SELECT id FROM tags WHERE name='fizyka')),
        ((SELECT id FROM courses WHERE name='Jazda rowerem'), 
            (SELECT id FROM tags WHERE name='rozwoj osobisty')),
        ((SELECT id FROM courses WHERE name='Kurs C++'), 
            (SELECT id FROM tags WHERE name='c++')),
        ((SELECT id FROM courses WHERE name='Kurs C++'), 
            (SELECT id FROM tags WHERE name='programowanie')),
        ((SELECT id FROM courses WHERE name='Kurs czytania'), 
            (SELECT id FROM tags WHERE name='edukacja')),
        ((SELECT id FROM courses WHERE name='Kurs czytania'), 
            (SELECT id FROM tags WHERE name='finanse')),
        ((SELECT id FROM courses WHERE name='Kurs czytania'), 
            (SELECT id FROM tags WHERE name='rozwoj osobisty')),
        ((SELECT id FROM courses WHERE name='Bazy danych'), 
            (SELECT id FROM tags WHERE name='programowanie')),
        ((SELECT id FROM courses WHERE name='Bazy danych'), 
            (SELECT id FROM tags WHERE name='rozwoj osobisty')),
        ((SELECT id FROM courses WHERE name='Bazy danych'), 
            (SELECT id FROM tags WHERE name='c++')),
        ((SELECT id FROM courses WHERE name='Bazy danych'), 
            (SELECT id FROM tags WHERE name='python'))
        """
    )


def downgrade():
    op.execute("DELETE FROM courses")
    op.execute("DELETE FROM trainings")
    op.execute("DELETE FROM participations")
    op.execute("DELETE FROM comments")
    op.execute("DELETE FROM course_tags")
