FROM python:3.8
RUN apt-get update && apt-get install -y wget
ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
RUN pip install poetry
RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY . .
RUN poetry config virtualenvs.create false \
  && poetry install
ENV FLASK_APP=flaskr
ENV FLASK_ENV=development
EXPOSE 5000
COPY docker-run.sh docker-run.sh
RUN apt-get update && apt-get install -y dos2unix && dos2unix docker-run.sh
RUN chmod +x  docker-run.sh;
CMD docker-run.sh

