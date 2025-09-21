FROM php:8.2-apache

COPY app/ /var/www/html/
COPY flag.txt /flag.txt
RUN chmod 444 /flag.txt /var/www/html/index.php