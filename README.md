# django-tutorial

A simple django app made mostly by following the official [Django tutorial](https://docs.djangoproject.com/en/1.11/intro/tutorial01/).

Additional stuff:
* REST api with [Django Rest Framework](http://www.django-rest-framework.org/).
* Swagger documentation with [django-rest-swagger](https://github.com/marcgibbons/django-rest-swagger).
* Unit tests with [pytest](https://docs.pytest.org/en/latest/).

## Usage
Clone the repo, create a virtualenv, migrate and spin up the Django development server.
```
git clone https://github.com/quvide/django-tutorial.git
cd django-tutorial

virtualenv venv
source venv/bin/activate

pip install -r requirements.txt

cd mysite
python manage.py migrate
python manage.py runserver
```

Tests can be ran with `pytest`.

## Caveats
Question choices can't be created with the API.
