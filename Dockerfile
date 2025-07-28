# Dockerfile
#create an image 
#start from env with py3.11
FROM python:3.11

#ignorer les pycache and display logs on cmd
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#cd /app
WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

#copie tous le project 
COPY . .
