# Docker file for the circleci python executor. It contains pre-installed
# the project dependencies as specified in requirements/main.md
# docker build . \
#   -t lifespline/praxis:exercise-template-python-executor \
#   -f .circleci/python_executor.Dockerfile
# docker push lifespline/praxis:exercise-template-python-executor

# syntax=docker/dockerfile:1
FROM python:3

WORKDIR /app

# install project requirements
COPY requirements/* ./
RUN pip install --no-cache-dir -r main.md
