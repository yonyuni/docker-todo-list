# syntax=docker/dockerfile:1

FROM python:3.9-alpine

# 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 작업 디렉토리 설정
WORKDIR /todo_list

# 의존성 설치
COPY requirements.txt /todo_list/
RUN pip install -r requirements.txt

# 소스 코드 복사
COPY . /todo_list/

EXPOSE 8000