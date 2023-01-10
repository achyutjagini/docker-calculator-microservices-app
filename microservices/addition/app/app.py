from flask import Flask

import flask.scaffold

flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func


from flask_restful import Api, Resource

class Addition(Resource): 
	def get(self, num1, num2):
		return {'result': int(num1) + int(num2)} #server will return the sum of two numbers as a JSON object


app = Flask(__name__)
api = Api(app)
api.add_resource(Addition, '/<num1>/<num2>')


#This code is the entry point for the Flask application. It runs the Flask development
# server in debug mode, listening on all available interfaces on port 5051. 
# When the application is run, it will listen for incoming HTTP requests
#  and route them to the appropriate resources based on the defined routes 
# and their associated methods.

#The if __name__ == "__main__": block is a standard Python idiom that ensures
#  that the code within it is only executed when the script is run directly, 
# rather than imported as a module. This allows the script to be used as both
#  an importable module and an executable script.

#For example, you can start the Flask development server by running the script with the Python interpreter:
#python app.py


#you can import the script as a module and call the run() method of the app object:
#import app
#app.run()

if __name__ =="__main__":
	app.run(debug=True,port=5051,host="0.0.0.0")
