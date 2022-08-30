FROM python:3-alpine

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN echo "Hello world" \
    > /app/hello.txt

CMD python3 main.py