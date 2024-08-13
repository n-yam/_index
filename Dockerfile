FROM python:3.12-alpine

COPY main ./main
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["flask", "--app", "main/wsgi.py", "run", "--host", "0.0.0.0"]