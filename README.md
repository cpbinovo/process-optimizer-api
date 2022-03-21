# Process Optimizer REST API

This project expose a REST based API for [ProcessOptimizer](https://github.com/novonordisk-research/ProcessOptimizer)

# How do I get started

If you have Docker installed the API can be started locally by running the script `build-and-run.sh`

Alternatively the project can be build and run with the following commands:

    python3 -m venv env
    source env/bin/activate
    pip install --upgrade pip

    pip install -r requirements-freeze.txt
    python -m optimizerapi.server

Now open [http://localhost:9090/v1.0/ui/](http://localhost:9090/v1.0/ui/) in a browser to explore the API through Swagger UI

# Running tests

Unit tetsts are located in the "tests" folder and can be run witht the following command

    python -m pytest

or use pytest-watch for continuously running tests

    ptw

# Building docker container

    docker build -t process-optimizer-api --build-arg GITHUB_REF_NAME=$(git describe --always) .

# Obtain encryption key

Run server once and extract a fresh encryption key from the logs.

    python -m optimizerapi.server

or using docker

    docker run --rm -it process-optimizer-api

# Running in production

Running using python

    FLASK_ENV=production PICKLE_KEY=<key from previous step> python -m optimizerapi.server

or use docker

    docker run -d --name process-optimizer-api --env PICKLE_KEY=<key from previous step> -p 9090:9090 process-optimizer-api:latest

# Use job queue

The API server supports distributing the calculation tasks using a Redis backed job queue.
To start the API server in "job queue mode" set the environment variable `USE_WORKER=true` and start the server and any number of
worker threads using the following commands:

    USE_WORKER=true python -m optimizerapi.server
    python -m optimizerapi.worker

The Redis server can be controlled through the environment variable `REDIS_URL` which defaults to `redis://localhost:6379`

# Adding or updating dependencies

When adding a new dependency, you should manually add it to `requirements.txt` and then run the following commands:

    pip install -r requirements.txt
    pip freeze | grep --invert-match pkg_resources > requirements-freeze.txt

Now you should check if the freeze operation resulted in unwanted upates by running:

    git diff requirements-freeze.txt

After manually fixing any dependencies, you should run:

    pip install -r requirements-freeze.txt

Remember to commit both the changed `requirements.txt` and `requirements-freeze.txt` files.

# Updating the change log

In order to keep the overhead of maintaining the change log as low as possible this project use a tool to automatically generate
as much of the change log as possible.

Before creating a new release please run the following command inside a clean working directory

    docker run -it --rm -v "$(pwd)":/usr/local/src/your-app githubchangeloggenerator/github-changelog-generator --user BoostV --project process-optimizer-api
