FROM python:3.10.4-slim
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ENV FLASK_APP=/usr/src/app/src/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
COPY . /usr/src/app
COPY migrate_db.sh /usr/bin
RUN pip install -e .
EXPOSE 5000
CMD ["./run_app.sh"]
