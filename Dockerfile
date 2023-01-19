FROM python:3.10.9-buster 
RUN apt-get update && apt-get -y install libpq-dev curl
RUN apt-get -y install gcc

WORKDIR /app

ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY /app /app/
ENV PYTHONPATH "${PYTHONPATH}:/Users/ericvincent/infra/infra/app/"

ENTRYPOINT ["python", "main.py" ]