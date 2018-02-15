![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# django-politico-civic-vote

Votes. votes. votes. We got the votes.

### Quickstart

1. Install the app.

  ```
  $ pip install django-politico-civic-vote
  ```

2. Add the app to your Django project and configure settings.

  ```python
  INSTALLED_APPS = [
      # ...
      'rest_framework',
      'entity',
      'geography',
      'government',
      'election',
      'vote',
  ]

  #########################
  # vote settings

  VOTE_API_AUTHENTICATION_CLASS = 'rest_framework.authentication.BasicAuthentication' # default
  VOTE_API_PERMISSION_CLASS = 'rest_framework.permissions.IsAdminUser' # default
  VOTE_API_PAGINATION_CLASS = 'vote.pagination.ResultsPagination' # default
  ```


### Developing

##### Running a development server

Move into the example directory, install dependencies and run the development server with pipenv.

  ```
  $ cd example
  $ pipenv install
  $ pipenv run python manage.py runserver
  ```

##### Setting up a PostgreSQL database

1. Run the make command to setup a fresh database.

  ```
  $ make database
  ```

2. Add a connection URL to `example/.env`.

  ```
  DATABASE_URL="postgres://localhost:5432/vote"
  ```

3. Run migrations from the example app.

  ```
  $ cd example
  $ pipenv run python manage.py migrate
  ```
