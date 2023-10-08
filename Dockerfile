FROM python:3.8
COPY ./app .

RUN pip install -r requirements.txt
CMD uvicorn app:app --host 0.0.0.0 --port 8080 --reload
