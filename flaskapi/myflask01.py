# only going to import a PIECE of the flask library

from flask import Flask

#FLASK == to app we are about to build!

#app is the variable that represents out website that we are building! 
#we want to "teach" out app object how we want it to behave

app= Flask(__name__)


#GOAL: 
# add a page tp my website that displays the message "hello world" 

# Decorators

@app.route("/bruno")
def hello_world():
    return "Hello world!"


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE
