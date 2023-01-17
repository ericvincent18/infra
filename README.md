![AppVeyor tests](https://img.shields.io/appveyor/tests/ericvincent18/infra)
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/ericvincent18/infra/ci.yml)
![Codecov](https://img.shields.io/codecov/c/github/ericvincent18/infra)
# Postgres, rabbitmq, PgAdmin, Docker

This repository contains code related to the creation of a Postgres database, PgAdmin UI to interact with the database, and finally a rabbitmq message broker to send and save data to the database. The data used in the following code can be found here : https://www.kaggle.com/datasets/zynicide/wine-reviews


Follow these steps to initialize the services

Virtual environment
1. Spin up a python venv > 3.8. `python3 -m venv virtualenv` then `source virtualenv/bin/activate`

Alembic
2. Create the following file under the directory /app/ : config --> config.py. Add the db connection string that will be used to create the migrations using alembic.
3. In the app folder, run `alembic init .`. In the alembic.ini file created, update the sqlalchemy.url.

Docker Compose
4. Create a .env file in the root of the project, add the following information (can also be added directly to the docker-compose file as environment variables) 
`POSTGRES_USER=
POSTGRES_PW=
POSTGRES_DB=
PGADMIN_MAIL=
PGADMIN_PW=
PGADMIN_DEFAULT_EMAIL=
PGADMIN_DEFAULT_PASSWORD=`

4. run `docker compose up` in the root directory.
5. The PgAdmin server can then be accessed at localhost:5050, using the credentials listed previously in .env
6. Connect to the Postgres db using the credentials listed in the .env file.

Migrations
7. Run `alembic upgrade head` to initialize the migrations. 

Main
Messages can be sent using `python new_task.py` 
Messages can be received and saved to the db running `python main.py`. The messages will be saved to the db using the psycopg2 and sqlalchemy clients.

