FROM python:3.12-alpine

COPY index ./index
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["flask", "--app", "index/wsgi.py", "run", "--host", "0.0.0.0"]