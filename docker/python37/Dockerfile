FROM python:3.7
WORKDIR /flaskapi
ENV APP_CONFIG=config/dev.conf
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
