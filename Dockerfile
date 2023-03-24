FROM python:3

RUN apt-get update && apt-get install -y git cmake pkg-config libsndfile1

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "waitress-serve", "server:app" ]