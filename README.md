# Developing and Testing an Asynchronous API with FastAPI and Pytest

## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/fastapi-crud).

## Want to use this project?

Build the images and run the containers:

```sh
$ docker-compose up -d --build
```

Test out the following routes:

1. [http://localhost:8002/ping](http://localhost:8002/ping)
1. [http://localhost:8002/docs](http://localhost:8002/docs)
1. [http://localhost:8002/notes](http://localhost:8002/notes)


## Want to use pre-commit?
For using the pre-commit, you should go inside of the `src` folder:
```bash
    # Create the environment
    python3 -m venv venv

    # Activate the environment
    source env/bin/activate

    # Install pre-commit
    pip3 install pre-commit
```