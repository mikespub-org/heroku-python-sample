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

## Deploying to Cloud Foundry

Create .cfignore to ignore files / directories as needed

```sh
$ cf push python-sample --random-route
```

- [Python Buildpack](https://docs.cloudfoundry.org/buildpacks/python/index.html)

## Deploying to Docker with CF Local plugin

Create local.yml with latest buildpack

```sh
$ sudo cf local stage python-sample
$ sudo cf local run python-sample -i 0.0.0.0 -p 8080
```

- [CF Local Plugin](https://github.com/cloudfoundry-incubator/cflocal)

## Building with Cloud Native Buildpacks

See [Turn Your Code into Docker Images with Cloud Native Buildpacks](https://blog.heroku.com/docker-images-with-buildpacks) and [An App’s Brief Journey from Source to Image](https://buildpacks.io/docs/app-journey/)

[Install Pack.](https://buildpacks.io/docs/tools/pack/)

Create [project.toml](project.toml) to exclude/include files for the image, specify buildpacks etc.

Adapt [Procfile](Procfile) to bind gunicorn to 0.0.0.0 if you want to use heroku buildpacks:

```
$ cat Procfile
web: gunicorn app:app -b 0.0.0.0:8000
```

Build (and optionally publish) container image with appropriate builder:

```
$ pack build --builder heroku/buildpacks mikespub/heroku-python-sample
latest: Pulling from heroku/buildpacks
...
===> ANALYZING
[analyzer] Restoring data for SBOM from previous image
===> DETECTING
[detector] heroku/python 0.0.0
===> RESTORING
[restorer] Restoring metadata for "heroku/python:shim" from cache
[restorer] Restoring data for "heroku/python:shim" from cache
===> BUILDING
[builder] -----> Using Python version specified in runtime.txt
...
[builder] -----> Installing requirements with pip
===> EXPORTING
...
[exporter] Setting default process type 'web'
[exporter] Saving mikespub/heroku-python-sample...
[exporter] *** Images (8b8f78fac102):
[exporter]       mikespub/heroku-python-sample
[exporter] Adding cache layer 'heroku/python:shim'
Successfully built image mikespub/heroku-python-sample
```

Test the containerized app image with Docker:

```
$ docker run --rm -p 8080:8000 mikespub/heroku-python-sample
[2022-11-21 16:34:31 +0000] [1] [INFO] Starting gunicorn 20.1.0
[2022-11-21 16:34:31 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
...
```

