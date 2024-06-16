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


### pip freeze

asgiref==3.8.1
attrs==23.2.0
brazilcep==6.2.0
certifi==2024.2.2
charset-normalizer==3.3.2
dj-database-url==2.1.0
Django==4.2.11
django-bootstrap5==23.4
django-heroku==0.3.1
geographiclib==2.0
geopy==2.4.1
googlemaps==4.10.0
humanize==4.6.0
idna==3.6
isodate==0.6.1
lxml==5.1.0
nominatim==0.1
platformdirs==4.2.0
psycopg2==2.9.9
pycep-correios==5.2.0
python-dotenv==1.0.1
pytz==2024.1
requests==2.31.0
requests-file==2.0.0
requests-toolbelt==1.0.0
six==1.16.0
sqlparse==0.4.4
tk==0.1.0
typing_extensions==4.10.0
urllib3==2.2.1
whitenoise==6.6.0
zeep==4.2.1