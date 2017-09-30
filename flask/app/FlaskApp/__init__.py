import os
from flask import Flask, request
from flask_restful import Resource, Api

UPLOAD_FOLDER = '/var/www/flask/FlaskApp/images'

app = Flask(__name__)
api = Api(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class File(Resource):
	def post(self):
		file = request.files['file'] 
		filename = file.filename 
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		return {'message': filename + ' successfully saved !'}

api.add_resource(HelloWorld, '/')
api.add_resource(File, '/upload')

if __name__ == "__main__":
    app.run(debug=True)