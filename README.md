# Polaris Project Template

This project contains the minimum boilerplate code needed to run an anchor using [django-polaris](https://https://github.com/stellar/django-polaris) version 2.

## Installation

* Fork this repository
* Rename the repository by going to the forked repository's settings tab
* `git clone https://github.com/<YOUR USERNAME>/<RENAMED PROJECT>.git`
* Install Python 3.7
* `cd <RENAMED PROJECT>`
* Run `pip install pipenv && pipenv install`

## Required Customizations

* Copy the environment file `cp anchor/.env-template anchor/.env`
* Add the Django and Polaris environment variables required:
    - [`DJANGO_SECRET_KEY`](https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-SECRET_KEY)
    - Any of the [Polaris environment variables](https://django-polaris.readthedocs.io/en/v1.6.0/#environment-variables) listed as required for the SEPs you'd like to support
* Implement and register your custom integration functions and classes
    - From the [docs homepage](https://django-polaris.readthedocs.io/en/v1.6.0/), select the SEPs you'd like to support to see the available integration functions and classes
    - [Register](https://django-polaris.readthedocs.io/en/v1.6.0/register_integrations/index.html) your implemented integrations
* If running a SEP-24 or SEP-6 anchor, uncomment the associated services in `docker-compose.yml`


## Using Docker

You can use Docker and docker-compose for local development:

* `docker-compose build`
* `docker-compose up`

