# index
Index is an app that supports your memorization efforts.


## Build
```
git clone https://github.com/n-yam/index.git
cd index
docker build -t index:0.0.1 .
```

## Run
```
docker run -p 8000:8000 --name index --rm index:0.0.1
```