docker compose stop db
docker container rm ml_db
docker volume rm masterlab_db
docker compose up db -d
