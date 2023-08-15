#the container should be based on the official Python 3.9 slim image. The "slim" variant of the image contains only essential components, which helps to keep the image size small.
FROM python:3.9-slim


WORKDIR /app

COPY requirements.txt .
COPY requirements-test.txt .

RUN pip install -r requirements.txt
RUN pip install -r requirements-test.txt

COPY . .

CMD [ "python", "main.py" ]


