FROM python:3.7

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . . 

ENTRYPOINT [ "python3", "app.py" ]
