# Polaris Project Template

This project contains the minimum boilerplate code needed to run an anchor using [django-polaris](https://https://github.com/stellar/django-polaris) version 1.6.

## Installation

1. Fork this repository
2. Rename the repository by going to the forked repository's settings tab
3. `git clone https://github.com/<YOUR USERNAME>/<RENAMED PROJECT>.git`
4. Install Python 3.7
5. `cd <RENAMED PROJECT>`
6. Run `pip install pipenv && pipenv install`

## Required Customizations

1. Copy the environment file `cp anchor/.env-template anchor/.env`
2. Add the Django and Polaris environment variables required:
  - [`DJANGO_SECRET_KEY`](https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-SECRET_KEY)
  - Any of the [Polaris environment variables](https://django-polaris.readthedocs.io/en/v1.6.0/#environment-variables) listed as required for the SEPs you'd like to support
3. Implement and register your custom integration functions and classes
  - From the [docs homepage](https://django-polaris.readthedocs.io/en/v1.6.0/), select the SEPs you'd like to support to see the available integration functions and classes
  - [Register](https://django-polaris.readthedocs.io/en/v1.6.0/register_integrations/index.html) your implemented integrations
4. If running a SEP-24 or SEP-6 anchor, uncomment the associated services in `docker-compose.yml`


## Using Docker

You can use Docker and docker-compose for local development:

`docker-compose build`
`docker-compose up`

