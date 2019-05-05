# Flask API for Elasticsearch
This repo contains the source code for the flask backend component.  It depends on the elasticsearch docker container in the parent repo.

## Requirements
* Docker

## Usage
You can stand up the container as follows:

```bash
$ docker-compose up --build
```

## Routes
The API is a (mostly) RESTful API, with document types of `review`, `business`, `user`, `checkin`, `tip`.
To request a document, simply make a GET request to the appropriate endpoint:

```
GET localhost:45000/doc/reviews/1000
```

You can update and delete documents by calling `PUT` and `DELETE` respectively.

You can hit the generic search endpoint to search across the `reviews` and `businesses` indexes.
Businesses are boosted 2x.  You can also use `offset` and `page_size` query params for pagination.

``` 
GET  localhost:45000/search?q=vegas%20pet%20spa
```