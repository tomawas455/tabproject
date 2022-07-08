FROM python:3.10.4-slim
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ENV FLASK_APP=/usr/src/app/src/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
ENV TAB_DB_URL='postgresql://postgres:postgres@db:5432/tabproject'
ENV TAB_SECRET_KEY='04105b8b7bcfa615a1d8e1065f08ef1560e0fa10033c6daf84c44174fa5f07e1f8a641e0b9887f48f0f8faeea21f1f817ee8b9d26def88854eeed8bb9050c7ca'
COPY . /usr/src/app
COPY migrate_db.sh /usr/bin
RUN pip install -e .
EXPOSE 5000
CMD ["./run_app.sh"]