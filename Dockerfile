FROM python:3
ADD . /code
WORKDIR /code
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
CMD python app.py
#RUN flask db upgrade -d src/infra/orm/migrations

COPY . /usr/src/app/