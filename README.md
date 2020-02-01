# SuervreuS 

 Suervreus is an IoT command service that runs on Python Flask. 
 
 
## Details

 The goal of this application is to give the ability to register clients and queue commands for these clients. The idea originated from an attempt at using IFTTT to allow a Google Home to control a client connected to my local network (such as a Raspberry Pi, Arduino, or ESP8266).

## Local Setup

#### Installation

Make sure `pip` is installed

Install `pyenv-virtualenv`, `memcached` and `sqlite3`


```
brew update
brew install sqlite3
brew install memcached
brew install pyenv-virtualenv
```

#### Create the Database

You may create the database with a filename other than `suervreus.db` but
you must update `DATABASE_FILENAME` in `config.py` with the name you use.

```
sqlite3 suervreus.db < schema.sql
```


#### Start the Cache

```
memcached -u memcached -d -m 30 -l 127.0.0.1 -p 11211
```


#### Virtual Enviroment

Make sure you are in the project directory.


Install the latest version of Python with `pyenv` if you have not installed `pyenv` before make sure to follow the instructions [here](https://github.com/pyenv/pyenv#installation).

```
pyenv install 3.8.1
```

Create a virtual environment

```
pyenv virtualenv 3.8.1 suervreus
```


Set virtual environment to auto activate when you are in the project directory

```
pyenv local suervreus
```


#### Python dependencies

```
pip install -r requirements.txt
```

#### Start the application

Set environment variables

```
export FLASK_APP=src/__init__.py
export FLASK_ENV=development
```

```
flask run
```
