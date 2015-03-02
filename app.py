from flask import Flask

# create the application object
app = Flask(__name__)

# use decorators to link the functions to an url
@app.route("/")
@app.route("/hello")
# define the view using a function
def hello():
    return "Hello World!"

# start the development server unsing the run() method
if __name__ == "__main__":
    app.run()
