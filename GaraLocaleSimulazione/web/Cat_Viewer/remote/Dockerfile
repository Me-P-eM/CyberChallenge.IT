FROM php:8.2-apache

RUN apt-get update && apt-get install -y default-mysql-client \
    && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-install pdo pdo_mysql

COPY app/ /var/www/html/
COPY flag.txt /flag.txt
RUN chmod 444 /flag.txt
RUN chmod -R 755 /var/www/html/images