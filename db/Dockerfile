FROM ubuntu


RUN apt-get update && apt-get install -y python3-pip wget

RUN pip3 install pymongo

COPY app.py app/app.py
WORKDIR /app

CMD [ "python3", "app.py" ]