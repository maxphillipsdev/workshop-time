FROM python:slim


WORKDIR /usr/src/app


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src/ src/

ENV FLASK_APP=src/app.py

CMD python src/app.py
