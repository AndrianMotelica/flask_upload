# from flask import Flask, request
# from flask_restful import Resource, Api

# app = Flask(__name__)
# api = Api(app)


# @app.route('/test', methods = ['GET', 'POST'])
# def test():
#       return 'test message'

# class File(Resource):
# 	def get(self):
# 		return 'get method'
# 	def post(self):		
# 		f = request.files['file'] #f.save(f.filename)	    
# 		return f
	 

# class Product(Resource):
# 	def get(self):
# 		return {'products': ["bread", "butter", "coffee"]}

# api.add_resource(Product, '/')
# api.add_resource(File, '/upload')

# if __name__ == '__main__':
# 	app.run(debug=True)