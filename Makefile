.PHONY: init-container
init-container:
	docker start my-lynks-python

.PHONY: init-flask
init-flask:
	docker exec my-lynks-python cd routes/
	docker exec my-lynks-python flask --app application run --host 0.0.0.0