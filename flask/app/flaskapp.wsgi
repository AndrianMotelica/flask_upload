#!/usr/bin/python
import sys
import logging
sys.stdout = sys.stderr
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/flask/")

from FlaskApp import app as application
application.secret_key = 'asd561sSDFzx4556'
