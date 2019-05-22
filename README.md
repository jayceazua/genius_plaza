# genius_plaza

1. docker-compose up -d --build
2. docker-compose run web python /code/manage.py migrate --noinput
3. docker-compose run web python /code/manage.py createsuperuser
4. docker build . or docker-compose build --no-cache 
5. docker-compose up
