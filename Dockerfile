# Dockerfile , image , container

FROM python:3

ADD main.py .

RUN pip3  install Flask python-dotenv pyjwt

CMD [ "python", "./main.py" ]