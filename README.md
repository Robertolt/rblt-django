rblt-django
applying django in a real project

aplication available on https://pyrbltdjango.herokuapp.com/

[![Updates](https://pyup.io/repos/github/Robertolt/rblt-django/shield.svg)](https://pyup.io/repos/github/Robertolt/rblt-django/)
[![Python 3](https://pyup.io/repos/github/Robertolt/rblt-django/python-3-shield.svg)](https://pyup.io/repos/github/Robertolt/rblt-django/)
[![Build Status](https://www.travis-ci.com/Robertolt/rblt-django.svg?branch=main)](https://www.travis-ci.com/Robertolt/rblt-django)
[![codecov](https://codecov.io/gh/Robertolt/rblt-django/branch/main/graph/badge.svg?token=HDBTH5ECGB)](https://codecov.io/gh/Robertolt/rblt-django)

-- enable travis CI, codecov and pyup
-- Install pyenv
-in cmd: pyenv global
-pip install pipenv
-pip install django
-pip install --dev flake8
--sync dev dependencies
-pipenv sync -d
-activating virtual env: pipenv shell (4 exit: "exit")
--run cmds in virtual env: pipenv run ......
--pipenv shell -> django-admin -> django-admin startproject pyrblt .
--to test django installation python manage.py runserver
--edit .bashrc (cat .bashrc) and add python manage.py runserver
--install heroku
--create Procfile text file with web: gunicorn pyrblt.wsgi ==log=file =
-pipenv install gunicorn
--heroku apps:create name()
-git push heroku main -f
-heroku config:set DISABLE_COLLECTSTATIC=1
-heroku open
--cd pyrblt/
-mng startapp base