run:
	pipenv run python -m project

docker_start_db:
	docker-compose -f docker-compose.yml up -d postgres

docker_stop_db:
	docker-compose -f docker-compose.yml stop postgres