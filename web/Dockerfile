FROM python:2

RUN mkdir -p /usr/src/web
WORKDIR /usr/src/web

COPY . .

RUN pip install -r requirements.txt


EXPOSE 5000

CMD ["uwsgi", "-s", "/tmp/web.sock", "--manage-script-name", "--mount", "/web=app:app", "--http", ":5000", "--master", "--processes", "4", "--threads", "2"]