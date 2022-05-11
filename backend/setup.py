from setuptools import setup

setup(
    name='tabproject',
    version='0.1',
    py_modules=['tabproject'],
    entry_points={
        'console_scripts': ['tabproject = tabproject:run']
    },
    install_requires=[
        'Flask==2.1.0',
        'Flask-SQLAlchemy==2.5.1',
        'Flask-Migrate==3.1.0',
        'Flask-Cors==3.0.10',
        'psycopg2-binary==2.9.3',
        'Werkzeug==2.0.3'
    ]
)
