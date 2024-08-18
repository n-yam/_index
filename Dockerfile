# Webpack
FROM node:20.16-alpine AS build

WORKDIR /work

COPY gui/package.json .
COPY gui/webpack.config.js .
COPY gui/src ./src

RUN npm install
RUN npm run build

# Flask
FROM python:3.12-alpine

COPY index ./index
COPY requirements.txt .
COPY --from=build /work/dist ./index/static

ENV TZ=Asia/Tokyo

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "index.wsgi", "--bind", "0.0.0.0"]