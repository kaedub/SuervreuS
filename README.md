# SuervreuS 

 Suervreus is an IoT command service that runs on Python Flask. 
 
 
## Documentation
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

#### Setup

Clone the repo then `cd SuervreuS`

Create virtual environment

```
pyenv virtualenv SuervreuS
```

Install Python dependencies

```
pip install -r requirements.txt
```

Set environment variables

```
export FLASK_APP=src/__init__.py
export FLASK_ENV=development
```

Start memcached

```
memcached -u memcached -d -m 30 -l 127.0.0.1 -p 11211
```

Run the application

```
flask run
```

