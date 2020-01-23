# SuervreuS 

 Suervreus is an IoT command service that runs on Python Flask. 
 
 
## Documentation
 The goal of this application is to give the ability to register clients and queue commands for these clients. The idea originated from an attempt at using IFTTT to allow a Google Home to control a client connected to my local network (such as a Raspberry Pi, Arduino, or ESP8266).

## Local Setup

#### Installation

Make sure `pip` is installed

Install `pyenv-virtualenv`, and `sqlite3`


```
brew update
brew install sqlite3
brew install pyenv-virtualenv
```

#### Setup

Setup virtual environment


```
pyenv virtualenv SuervreuS
```

Environment variables

```
export FLASK_APP=src/__init__.py
export FLASK_ENV=development
```

Run the application

```
cd SuervreuS
flask run
```

