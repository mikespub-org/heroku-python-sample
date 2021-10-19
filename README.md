# Python: Getting Started

A barebones Flask app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python 3.9 [installed locally](https://docs.python-guide.org/starting/installation/). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

```sh
$ git clone https://github.com/heroku/python-sample.git
$ cd python-sample

$ python3 -m venv venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt

$ # createdb python_getting_started

$ # python manage.py migrate
$ # python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create  # first time only
$ git add .
$ git commit -m "update repo"
$ git push heroku master

$ # heroku run python manage.py migrate
$ heroku logs --tail
$ heroku run bash
$ # heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
