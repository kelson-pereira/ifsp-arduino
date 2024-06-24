# ifsp-arduino

## IFSP, 2024
### Articulando o ensino de física com a plataforma Arduino
### Projeto Final


### Comandos de instalação do python3:

brew update && brew install python3 && brew cleanup phyton3 && python3 --version


### Comandos de instalação do django e demais componentes:

pip3 install Django --break-system-packages

pip3 install whitenoise --break-system-packages

pip3 install dj-database-url --break-system-packages

pip3 install django-heroku --break-system-packages


### Comandos de inicialização do projeto:

django-admin startproject ifsp_arduino

mv ifsp_arduino ifsp-arduino && cd ifsp-arduino

django-admin startapp labclima


### Comandos para execução do projeto localmente:

cd ifsp-arduino

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py collectstatic --noinput --clear

python3 manage.py runserver 0.0.0.0:8000


### Comandos para recriar banco de dados:

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete 

find . -path "*/migrations/*.pyc" -delete

find . -path "*/db.sqlite3" -delete

python3 manage.py makemigrations labclima

python3 manage.py migrate


### Comandos para criar banco de dados na plataforma Heroku:

heroku login

heroku run python manage.py makemigrations --app labclima

heroku run python manage.py migrate --app labclima

heroku logs --app labclima --tail