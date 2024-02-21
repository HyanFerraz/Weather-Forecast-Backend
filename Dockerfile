FROM python:3.11.2
RUN pip install --upgrade pip

COPY .env .env
COPY requirements.txt requirements.txt 
COPY src /src
RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python3", "./src/main.py"]