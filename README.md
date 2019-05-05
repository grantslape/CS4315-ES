# CS4315-ES
This application indexes data from the Yelp dataset into an Elasticsearch cluster, and uses that instead of a database layer to serve up several different kinds of documents via a Flask REST API.  It also includes a mobile-friendly React frontend client made with `create-react-app`.

This application is **not** production ready.  It has no auth layer whatsoever, and doesn't use `https`.

## Requirements
* [Docker](https://docs.docker.com/)
* Docker Compose
* Python 3 (to seed the indices)
* `npm` (for the React frontend)
* [Yelp dataset](https://www.yelp.com/dataset/download)

## Setup
### Setting up Elasticsearch
First you'll need to build and start the Elasticsearch cluster.  From the project root:

```bash
$ docker-compose up --build -d
```

### Setting up the Flask API
Next you'll need to build and start the Flask API:

```bash
$ cd backend
$ docker-compose up --build -d
```

You can check that the API is working via the heartbeat route.  You can use cURL or Postman or whatever you prefer for making HTTP requests:

```
GET http://localhost:45000/
```

### Creating the Indices
Next we'll need to create the indices for our five document types.  You should do this through the Flask API rather than directly on the Elasticsearch, because the Flask API has some custom mappings that it will apply:

```
POST  http://localhost:45000/index/reviews
POST  http://localhost:45000/index/businesses
POST  http://localhost:45000/index/users
POST  http://localhost:45000/index/tips
POST  http://localhost:45000/index/checkins
```

### Indexing the Dataset
You'll need to download the dataset first.  Then you can begin seeding the indices.  From the project root:

```bash
$ mv /path/to/dataset/*.json scripts/
$ cd scripts
$ python3 -m venv env
$ source env/bin/activate
$ python seed-indices.py
```

Wait for the seeding jobs to finish.  Then you can deactivate the python virtual environment:

```bash
$ deactivate
```

Now you can test a simple GET on the Flask API to see an example document:

```
GET http://localhost:45000/doc/reviews/10000
```

### Setting up the React Frontend
The React frontend will give you a UI to search and view data via the Flask API and the Elasticsearch cluster.  You'll need to build it first, from the project root:

```bash
$ cd frontend
$ npm start
```

Then navigate to [http://localhost:3000](http://localhost:3000) in your browser to view the site.  It is optimized for mobile, so you may want to turn dev tools on and change the window size to a mobile viewport.
