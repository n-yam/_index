FROM python:3.12-alpine

COPY index ./index
COPY requirements.txt .

ENV TZ=Asia/Tokyo

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "index.wsgi", "--bind", "0.0.0.0"]