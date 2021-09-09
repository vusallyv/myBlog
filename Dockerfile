# FROM python:3.9
FROM python:3.9-slim

WORKDIR /

COPY . .
COPY /requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# ENV FLASK_APP=main.py

# ENV hi="hi"

# CMD [ "flask", "run" , "-h", "0.0.0.0", "-p", "5588"]
# CMD [ "flask", "run"]

# EXPOSE 5000