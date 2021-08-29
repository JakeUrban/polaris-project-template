FROM python:3.7

RUN apt-get update && apt-get install -y build-essential python3-dev

WORKDIR /code
COPY . .

RUN pip install pipenv && pipenv install && pipenv run python anchor/manage.py collectstatic --no-input

CMD pipenv run python anchor/manage.py runserver --nostatic 0.0.0.0:8000
