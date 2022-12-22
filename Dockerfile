FROM python:3.10.9-slim-buster
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app



# COPY . .
ENTRYPOINT [ "main.py" ]
CMD [ "python", "main.py" ]
