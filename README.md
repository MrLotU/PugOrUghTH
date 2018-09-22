# Pug or Ugh

To run the app, first start your pipenv and install deps:
```
pipenv install -r requirements.txt
```

Than to run the app:
```
pipenv run backend/manage.py migrate
pipenv run backend/manage.py runserver 0:8080
```
You can log in with user:
```
USERNAME: test
PASSWORD: 1234
```

To run the tests and get the code coverage, run:
```
pipenv run coverage run backend/manage.py test pugorugh
pipenv run coverage report
```