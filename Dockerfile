FROM python:3.7.7-slim

MAINTAINER salamander

WORKDIR /usr/src/app

COPY ./src .

RUN apt-get update
RUN apt-get install -y procps libglib2.0-0
RUN apt-get install -y libzbar0  # 安装Zbar
RUN pip install -i  https://pypi.doubanio.com/simple/ --no-cache-dir -r requirements.txt

CMD [ "uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]