FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir /code
WORKDIR /code

#Upgrade pip
RUN pip install pip -U
ADD requirements.txt /code/

#Install dependencies 
RUN pip install -r requirements.txt 
ADD . /code/

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev -y


