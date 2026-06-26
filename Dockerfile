FROM python:latest

RUN pip install sqlalchemy pydantic fastapi 

RUN apt-get update && apt-get install sqlite3

EXPOSE 8000

 

