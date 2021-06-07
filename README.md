# My First Django App

This playground was created from Django framework on Python3. This project was created with the tutorials
under https://docs.djangoproject.com/en/3.2/. [PostgreSQL](https://www.postgresql.org/) is preferred as database.

[django-environ](https://django-environ.readthedocs.io/en/latest/), [jsons](https://jsons.readthedocs.io/en/latest/)
, [gunicorn](https://gunicorn.org/) packages, **dataclass**, **csrf_exempt**, **register.simple_tag**, **admin.display**
decorators and one custom middleware and JsonResponse used.

Before you launch the application, you should check that your definitions in the **.env** are correct.

&nbsp;

Admin: http://localhost:8001/admin/

Polls: http://localhost:8001/polls/

&nbsp;
## Example API Requests
### Poll Create
``` 
curl --location --request POST 'http://localhost:8001/polls/api/add' \
--header 'X-Access-Token: always-better' \
--header 'Content-Type: application/json' \
--data-raw '{"author": "HSK", "questionText": "What'\''s up?", "status":1, "publishTime": "2020-06-08T11:30:59Z"}'
```

### Poll Detail
``` 
curl --location --request GET 'http://localhost:8001/polls/api/1/' \
--header 'X-Access-Token: always-better'
```

&nbsp;
## Useful Commands
### Migration
```
python3 manage.py makemigrations
python3 manage.py makemigrations polls
python3 manage.py sqlmigrate polls 0001
python3 manage.py migrate
```

&nbsp;
### Test
```
python3 manage.py test
```

&nbsp;
### Pre-Release
```
python3 manage.py collectstatic
pip3 freeze > requirements.txt
LDFLAGS=-L/opt/homebrew/opt/openssl@1.1/lib pip install  -r requirements.txt
```

&nbsp;
### How to create a super user?
```
python3 manage.py createsuperuser --username=admin --email=your@email.com
```

&nbsp;
### Start with lightweight development Web server
```
python3 manage.py runserver 0.0.0.0:8001
```

&nbsp;
### Start with Gunicorn
```
gunicorn --bind 0.0.0.0:8001 firstApp.wsgi
```