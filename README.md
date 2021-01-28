# aiohttp-docker

## CONTAIN

DOCKERFILE

aiohttp-sample/
  server.py
  client.py

1. server.py
  - aiohttp 비동기로 전송되는 간단한 이름을 반환하는 get

2. client.py
  - server.py 로컬에서 실행된 서버에서 asyncio를 이용해 요청을하고 받아옴.

## HOW TO RUN

1. make docker image
  - `docker build -t aiosample .`
 
2. run
  - `docker run -it --rm --name aio -v {now_pwd}:/aiohttp-sample aiosample /bin/bash`

3. do it
