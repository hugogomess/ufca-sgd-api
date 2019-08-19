# UFCA - Sistema de Gestão de Demandas (SGD)

Sistema de Gestão de Demandas da UFCA. 

## Dependencies

First of all, you need to have installed [Python 3.7.3](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installing/) on your machine.

To check the dependencies, use the commands `$ python --version` and `$ pip --version`.

## Installation

1. First clone this repository:

  ```
  $ git clone git@github.com:hugogomess/ufca-sgd-api.git
  ```

2. Go to the project directory:

  ```
  $ cd ufca-sgd-api
  ```

3. Solve the dependencys:

  ```
  $ pip install -r requirements-dev.txt
  ```

4. Create migrate

  ```
  $ python manage.py migrate
  ```

5. Create a super user

  ```
  $ python manage.py createsuperuser
  ```

## Use

1. Inside the project root folder, run:

  ```
  $ python manage.py runserver
  ```

2. In your browser, open [http://localhost:8000](http://localhost:8000).