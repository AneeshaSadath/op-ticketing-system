# OP Ticketing System
 This app is used for generating OP tickets for patients in hospitals. The generated OP tickets are saved in the project folder as text file. Each time, when an OP ticket is generated, it overwrites the previous ticket. i.e, the project folder will only have the recently generated OP ticket in it.
## Prerequisites

- [MongoDB Community Edition](https://www.mongodb.com/try/download/community)
- [Python v3.8.x](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/)
- [Rabbitmq](https://www.rabbitmq.com/)
- [Docker](https://docs.docker.com/engine/install/)
- [Celery](https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html#installing-celery)

Note: One can install all the above prerequisites using docker.
Instructions are provided below:

All dependencies required for the python project including [flask web framework](https://flask.palletsprojects.com/en/1.1.x/)  are  installed by poetry.

## Installation using Docker Compose

Here are the commands required for running docker-compose:
1. To start all the containers and app use -  `docker-compose up` 
2. To stop all the containers and app use -`docker-compose down`

## Install pre-commit hooks
After cloning the repository, run the following command to install pre-commit hook. This automatically runs 
[black](https://pypi.org/project/black/) and [flake8](https://flake8.pycqa.org/en/latest/) tools, which
perform code formatting. Make sure to  add the formatted files to git again.

```
poetry run pre-commit install 
```
## Verification
You should be able to access the server at http://localhost:5000/

## To run tests
Please type the following commands in a new terminal to run all the tests.

```
docker exec -it op-ticketing-system bash
pytest -v
```