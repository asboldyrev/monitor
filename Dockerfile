FROM nginx:1.21

RUN apt-get update -y

WORKDIR /usr/share/nginx/html
COPY ./vue-app/dist/ /usr/share/nginx/html/
