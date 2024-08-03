FROM python:latest
ENV PYTHONUNBUFFERED 1
ENV PIP_ROOT_USER_ACTION=ignore
WORKDIR /configservice
COPY requirements.txt /configservice/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /configservice