# Simple news board API.

To run the project install python version 3.7 and higher, docker and docker-compose

Clone the repository:
```bash
git clone https://github.com/azazellooo/news-api.git
```

After cloning, go to the cloned folder and run the following commands:


```bash
docker build .
docker-compose run web sh -c "python manage.py migrate"
docker-compose run web sh -c "python manage.py runserver"
```



Deployed API root: https://quicknewsapi.herokuapp.com/api/

