"""empty message

Revision ID: 1ab2ecdcdbdf
Revises: d61ba88f5408
Create Date: 2022-04-21 18:52:00.976296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ab2ecdcdbdf'
down_revision = 'd61ba88f5408'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """ INSERT INTO multimedias
        (filename, course_id) VALUES
        ('https://cdn.discordapp.com/attachments/966728087519760444/966729021813563433/unknown.png', 
            (SELECT id FROM courses WHERE name='Jazda rowerem')),
        ('https://cdn.discordapp.com/attachments/966728087519760444/966729390354485258/unknown.png', 
            (SELECT id FROM courses WHERE name='Kurs C++')),
        ('https://cdn.discordapp.com/attachments/966728087519760444/966729505072902184/unknown.png', 
            (SELECT id FROM courses WHERE name='Kurs C++')),
        ('https://cdn.discordapp.com/attachments/966728087519760444/966728310858088478/unknown.png', 
            (SELECT id FROM courses WHERE name='Bazy danych')),
        ('https://cdn.discordapp.com/attachments/966728087519760444/966729325380513802/unknown.png', 
            (SELECT id FROM courses WHERE name='Bazy danych')),
        ('https://cdn.discordapp.com/attachments/966728087519760444/966729746362822676/unknown.png', 
            (SELECT id FROM courses WHERE name='Kurs czytania')),
        ('https://cdn.discordapp.com/attachments/966728087519760444/966729863409041459/unknown.png', 
            (SELECT id FROM courses WHERE name='Kurs czytania')),
        ('https://cdn.discordapp.com/attachments/966728087519760444/966731944849178634/unknown.png', 
            (SELECT id FROM courses WHERE name='Kurs czytania')),
        ('https://cdn.discordapp.com/attachments/966728087519760444/966732139091619950/unknown.png', 
            (SELECT id FROM courses WHERE name='Kurs czytania')),
        ('https://cdn.discordapp.com/attachments/966728087519760444/966732277772075028/unknown.png', 
            (SELECT id FROM courses WHERE name='Kurs czytania')),
        ('https://cdn.discordapp.com/attachments/966728087519760444/966728553167204433/unknown.png', 
            (SELECT id FROM courses WHERE name='Jazda samochodem')),
        ('https://cdn.discordapp.com/attachments/966728087519760444/966729590502457384/unknown.png', 
            (SELECT id FROM courses WHERE name='Taniec ekstremalny'))
        """
    )

    op.execute(
        """ INSERT INTO meetings
        (begin_date, end_date, training_id) VALUES
        ('2022-03-12 11:50:00', '2022-03-12 13:50:00', '1'),
        ('2022-03-12 11:50:00', '2022-03-12 15:50:00', '2'),
        ('2022-11-05 07:45:00', '2022-11-05 15:50:00', '3'),
        ('2022-11-06 08:45:00', '2022-11-06 15:50:00', '3'),
        ('2022-11-07 08:45:00', '2022-11-07 15:50:00', '3'),
        ('2022-11-08 07:45:00', '2022-11-08 15:50:00', '3'),
        ('2022-10-30 14:45:00', '2022-10-30 15:50:00', '4'),
        ('2022-11-01 14:45:00', '2022-11-01 15:50:00', '4'),
        ('2022-11-03 14:45:00', '2022-11-03 15:50:00', '4'),
        ('2022-11-04 14:45:00', '2022-11-04 15:50:00', '4'),
        ('2022-04-15 11:50:00', '2022-04-15 15:50:00', '5')
        """
    )


def downgrade():
    op.execute("DELETE FROM multimedias")
    op.execute("DELETE FROM meetings")
