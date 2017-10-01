FROM debian:jessie

RUN apt-get update && \
	apt-get install -y vim npm apache2
RUN a2enmod headers rewrite && \
	service apache2 restart

RUN npm install angular angular-file-upload

COPY ClientApp.conf /etc/apache2/sites-available/ClientApp.conf

WORKDIR /var/www/ui
COPY . /var/www/ui

#enable clientapp site
RUN a2ensite ClientApp && \
	service apache2 restart 

# manage runable command file
COPY run.sh /opt/run.sh
RUN chmod +x /opt/run.sh

CMD ["/opt/run.sh"]