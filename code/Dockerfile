FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

ADD ./requirements.txt ./

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN rm requirements.txt

# CMD python run.py
CMD python create_db.py && \
    gunicorn -b 0.0.0.0:5000 -w 3 run:app