FROM php:7.4.28

RUN apt-get update -y && apt-get install -y openssl zip unzip git wget && apt-get autoclean
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
#RUN docker-php-ext-install

WORKDIR /app
RUN wget https://github.com/asboldyrev/monitor/archive/refs/heads/docker.zip && unzip docker.zip && rm docker.zip && mv /app/monitor-docker/* /app && rm -rf monitor-docker
RUN composer install --no-dev

CMD php -S 0.0.0.0:8181 -t public/
EXPOSE 8181