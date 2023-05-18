FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN apt-get -y update

RUN apt-get -y upgrade

RUN apt-get -y install ffmpeg

CMD uvicorn src.main:app --host 0.0.0.0 --port 8000
