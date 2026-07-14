.PHONY: build-dockerfile
build-dockerfile:
    docker build -t my-python-image .
    docker run --name my-lynks-python -p 5000 $(pwd):/app my-python-image

.PHONY: init-container
init-container:
    docker start my-lynks-python

.PHONY: init-flask
init-flask:
    docker exec -w /app/routes my-lynks-python flask --app application run --host 0.0.0.0