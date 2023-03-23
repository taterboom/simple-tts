FROM python:3

RUN apt-get update && apt-get install -y git cmake pkg-config libsndfile1

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python", "./server.py" ]