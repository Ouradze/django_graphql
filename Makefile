build:
	@docker-compose -p graphql-demo build
build-scratch:
	@docker-compose -p graphql-demo build --no-cache
run:
	@docker-compose -p graphql-demo up -d
stop:
	@docker-compose -p graphql-demo down
jupyter:
	@docker-compose run --rm -p 8888:8888 backend python manage.py shell_plus --notebook
clean-data:
	@docker-compose -p graphql-demo down -v
clean-images:
	@docker ps -a -q -f=name=graphql-demo | xargs -I {} docker rm {}
clean: clean-data clean-images
# Developpment
dev:
	@docker-compose -p graphql-demo up
test:
	@docker-compose run --rm backend pytest
quality:
	@docker-compose exec backend black --check
	@docker-compose exec backend flake8 .
	@docker-compose exec backend pylint .

