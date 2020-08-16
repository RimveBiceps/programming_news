# Programming news site

## Setting up:
### Virtual Environment

Step 1: Install Virtualenv
* sudo apt-get update
* sudo apt-get install python3-virtualenv

Step 2: Create a Virtual Environment
* virtualenv -p /usr/bin/python3 venv/project_1


Step 3: Activate Your Virtual Environment
* source venv/project_1/bin/activate

------------------------
### Django
Step 1: Install Django
* pip install django

Step 2: Check if django works
* django-admin

Step 3: Create django project
* django-admin startproject django_news

Step 4: Run django project
* cd django_news
* python3 manage.py runserver
------------------------
Create new django app
* python3 manage.py startapp news_app
