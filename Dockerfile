FROM python:3.10-bullseye

COPY . /app

ENTRYPOINT [ "app.py" ]

CMD [ "python",'app.py' ]