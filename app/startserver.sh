#!/usr/bin/env bash


SQLALCHEMY_DATABASE_URI=mysql+mysqlconnector://testapp:testapp@localhost/testapp gunicorn --bind 127.0.0.1:8000 --workers 3  wsgi:app
