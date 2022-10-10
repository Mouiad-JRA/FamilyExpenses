# FamilyExpenses

The goal of this project is to build a web site to track Family expenses, that everyone can use, which _just works_ out of the box and has the basic setup you can expand on. 

It's written with Django 4.1.1 and python 3.9 in mind.


### Main features

* Separated dev and production settings (soon)

* Example app with custom user model

* Bootstrap static files included

* User registration, logging in and logout

* Create a head of family member

* Head of the family can add or modify materials

* head of family can add or modify OutlayType

* head of family can add or modify Users

* Normal user can add, modify or delete his expense

* Provide Expenses within a specific month or year and show their total.

* Provide Private expenses for each user and show their total.

* Provide Special expenses for materials purchased and show their total.

* Provide Expenses for services + total expenses for services and show their sum.

* Customize the Entier admin Dashboard.

* Procfile for easy deployments

* Separated requirements files

* MySQL is used and SQLite by default if no env variable is set

# Usage

To use this project to start your own:

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install the requirements by running

    $ pip install -r requirements/requirements.txt
    
And create new mysql database then run the `python manage.py makemigrations` command to make the database tables then run:

    $ python manage.py migrate

      
### No virtualenv

we assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pipenv shell
    
After that just install the local dependencies

    $ pip install -r requirements/requirements.txt
    
And create new mysql database then run migrations using `python manage.py makemigrations` command then run:

    $ python manage.py migrate
      
# Quick Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/Mouiad-JRA/FamilyExpenses.git
    $ cd FamilyExpenses
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
    
For help getting started with Django, visit the online [documentation](https://docs.djangoproject.com/en/4.1/), which offers tutorials, samples, guidance on Backend development.
