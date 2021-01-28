FROM python:3

WORKDIR /aiohttp-sample
ADD ./requirements.txt /aiohttp-sample/
RUN pip install -r requirements.txt
