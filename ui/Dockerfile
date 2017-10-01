FROM debian:jessie

RUN apt-get update && \
	apt-get install -y vim npm bower apache2
RUN a2enmod headers rewrite && \
	service apache2 restart

COPY ClientApp.conf /etc/apache2/sites-available/ClientApp.conf

WORKDIR /var/www/ui
COPY . /var/www/ui

#enable clientapp site
RUN a2ensite ClientApp && \
	service apache2 restart 

CMD ["sh", "-c", "tail -f /dev/null"]