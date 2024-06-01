#!/bin/sh

# 데이터베이스 마이그레이션 수행
python manage.py migrate

# Gunicorn 실행
exec gunicorn my_project1.wsgi:application --bind 0.0.0.0:8000
