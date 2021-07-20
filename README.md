##Library Management System

Simple overview of project

## Description

this is a simple library management system

## Getting Started

### Installing

* Docker must be installed on your system
* Python3 must be installed on your system

#### 1. run this code to bulid project 

`
docker-compose build
`

#### 2. create super user for login in project
`
docker-compose run web python manage.py createsuperuser
`

#### 3. run this code to run server

`
docker-compose up
`


### or you can use this way
#### 1. install virtual environment

`
 py -m venv env
`

#### 2. active your env

`
env\Scripts\activate.bat
`

#### 3. install all dependency

`
pip install -r requirements.txt
`

#### 4. run server

`
python manage.py runserver
`

## Author

Alireza Ghasemi @Lyrdaqs
