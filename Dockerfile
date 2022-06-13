
FROM python:3.8.0-slim-buster
# 도커는 파이썬 설치되어 있는 이미지를 기본으로 제공 한다. 이 이미지를 불러온다

WORKDIR /user/src/app
# 프로젝트의 작업 폴더를 해당 경로로 지정한다.

ENV PYTHONDONTWRITEBYTECODE 1
# 파이썬은 종종 소스코드를 컴파일하여 확장자가 .pyc인 파일을 생성한다, 해당파일은 필요치 않으므로 .pyc 파일을 생성하지 않도록 한다.

ENV PYTHONUNBUFFERED 1
# 파이썬 로그가 버퍼링 없이 즉각적으로 출력하게 만든다.

COPY . /user/src/app/
# 로컬 컴퓨터의 현재위치(도커파일이 있는위치)에 있는 파일을 모두 작업폴더 (WORKDIR)로 복사 
# 그래야 지금껏 작성한 장고 프로젝트가 도커 이미지에 담긴다. (.)는 현재 폴더를 의미하고 경로는 복사할 작업 폴더를 의미한다 둘 사이 공백이 있다.

# install deptndencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# requirements.txt에 나열된 라이브러리들을 설치한다.

