FROM debian:jessie

#install apache and modules
RUN apt-get update && \
	apt-get install -y apache2 curl vim libapache2-mod-wsgi python-pip
	#python-flask

#enable modules
RUN a2enmod headers rewrite && \
	a2enmod wsgi && \
	service apache2 restart

COPY ./app /var/www/flask
WORKDIR /var/www/flask

#grant write to application folder
RUN chmod +w /var/www/flask/FlaskApp

#install python requirements
RUN pip install --upgrade -r requirements.txt

COPY FlaskApp.conf /etc/apache2/sites-available/FlaskApp.conf

#enable flaskapp site
RUN a2ensite FlaskApp && \
	service apache2 restart 

CMD ["sh", "-c", "tail -f /dev/null"]