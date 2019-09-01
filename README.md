# UFCA - Sistema de Gestão de Demandas (SGD)

Sistema de Gestão de Demandas da UFCA.

## Dependencias

Primeiramente, você precisa ter o [Python 3.7.3](https://www.python.org/downloads/) instalado no seu computador.

Para checkar as dependências use `$ python --version` e `$ pip --version`.

## Instalação

1. Clone esse repositório:

  ```
  git clone git@github.com:hugogomess/ufca-sgd-api.git
  ```

1. Vá até o diretório do projeto:

  ```
  $ cd ufca-sgd-api
  ```

1. Instale as dependências do projeto:

  ```
  $ pip install -r requirements-dev.txt
  ```

1. Crie a migração do banco de dados migrate

  ```
  $ python manage.py migrate
  ```

1. Crie um super usuário (todas as permissões)

  ```
  $ python manage.py createsuperuser
  ```

## Servidor de Desenvolvimento

1. Dentro da pasta do projeto, rode o comando:

  ```
  $ python manage.py runserver
  ```

No seu navegador vá até [http://localhost:8000](http://localhost:8000).
