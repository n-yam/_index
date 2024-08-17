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

## Usage
```
# Add new card
curl -XPOST localhost:8000/api/cards -F frontText="hello" -F backText="world" -F frontImage=@dog.jpg -F frontImage=@monkey.jpg -F backImage=@pheasant.jpg

# Update card
curl -XPUT localhost:8000/api/cards -F frontText="hello" -F backText="world" -F frontImage=@dog.jpg -F frontImage=@monkey.jpg -F backImage=@pheasant.jpg

# Get card
curl -XGET localhost:8000/api/cards/1

# Get all cards
curl -XGET localhost:8000/api/cards

# Delete card
curl -XDELETE localhost:8000/api/cards/1

# Get quesiton
curl -XGET localhost:8000/api/questions/first

# Answer Question
curl -XPOST localhost:8000/api/questions/first?answer=1  # succeed
curl -XPOST localhost:8000/api/questions/first?answer=0  # failed

# Get question count
curl -XGET localhost:8000/api/questions/count

# Reset questions
curl -XPOST localhost:8000/api/questions/reset
```