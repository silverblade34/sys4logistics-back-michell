FROM python:3.8.10

WORKDIR /app

RUN apt update && \
    apt install 

COPY requeriments.txt requeriments.txt

RUN pip3 install -r requeriments.txt

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]

