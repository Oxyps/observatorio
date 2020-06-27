# Observatório 👁‍🗨🎲

## Description 📜

This project is an implementation of my undergraduate thesis.
Which consists in visualize a large number of data in an easier way, through graphs.

## Open Data 🔓

The data analysed comes from a huge CSV file provided by [Brazilian Open Data Portal](www.dados.gov.br). This data went through an ETL proccess, by [Leonardo Gabriel Lubczyk](github.com/kyrosx/observatorio_etl), to be structured in the database.

## Technologies 🧰

  - [Python](docs.python.org/3/)
  - [MySql](dev.mysql.com/doc/)
  - [Django](docs.djangoproject.com/en/3.0/)
  - [Chart.js](chartjs.org/docs/latest/)

## Database Structure 🧱
![image-model-v3](https://user-images.githubusercontent.com/29782248/85910730-02ccc200-b7f7-11ea-8a28-ffb7ef7a51d4.png)

## First Steps 🧭

**Windows**

- Make sure you already have installed pip:
``` shell
> pip --version
```

- Install Pipenv environment package manager:
``` shell
> pip install pipenv
```

- Activate environment:
``` shell
> pipenv shell
```

- Check requirements:
``` shell
> pipenv check
```

- Install all project dependencies:
``` shell
> pipenv install
> pipenv install --dev
```

- Alter databases config to your `NAME`, `USER` and `PASSWORD` in settings.py, like:
``` python
NAME = 'observatorio'
USER = 'root'
PASSWORD = ''
```

- Create the database `NAME` in your server:
``` sql
CREATE DATABASE observatorio DEFAULT CHARACTER SET utf8mb4;
```

- Run migrations:
``` shell
> py manage.py migrate
```

- Run server:
``` shell
> py manage.py runserver
```
