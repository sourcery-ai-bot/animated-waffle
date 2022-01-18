

run Dockerfile

in project directory run:
```
docker-compose up -d --build
```

secondly, run:
```
docker-compose exec web python manage.py collectstatic
```


Then, run:
```
docker-compose exec web python manage.py migrate
```

finally, run:
```
docker-compose up -d --build
```






