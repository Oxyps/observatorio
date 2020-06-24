1 - Make sure you already have installed pip:
pip --version

2 - Install Pipenv environment package manager:
pip install pipenv

3 - Check requirements:
pipenv check

4 - Install all project dependencies:
pipenv install
pipenv install --dev

5 - Run migrations:
py manage.py migrate

6 - Run server:
py manage.py runserver
