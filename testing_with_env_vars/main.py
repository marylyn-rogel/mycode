#This imports the Flask class from the flask module. 
from flask import Flask

#This imports the os module, which provides a way to interact with the operating system, including accessing environment variables.
import os

#This creates an instance of the Flask class and assigns it to the variable app. The __name__ argument is used to determine the root path for the application.
app = Flask(__name__)

#This is a decorator
#It associates the hello() function with a specific route in the web application.
#The route is '/', which represents the root URL of the application.
@app.route('/')
#This defines a function named hello. It will be executed when a request is made to the route. 
def hello():  
    my_variable = os.getenv('MY_VARIABLE', 'default_value')  # the second argument is a default value if the environment variable isn't set. 
    return f"Hello, {my_variable}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2224)

