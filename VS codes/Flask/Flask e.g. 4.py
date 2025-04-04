# we want that our function first takes the input and then executes

from flask import Flask  # Importing the Flask module to create a web application 
from flask import request  # Importing request module to handle URL parameters

app = Flask(__name__)  # Creating a Flask app instance

@app.route("/")  # Defining the route for the root URL "/"
def greet():  # Function to handle requests at "/"
    return "<h1>Hello, Everyone</h1>"  # Returning an HTML response

@app.route("/how-are-you")  # Defining the route "/how-are-you"
def ask_well():  # Function to handle requests at "/how-are-you"
    return "<h1>How are you?</h1>"  # Returning an HTML response

@app.route("/how-was-your-day")  # Defining the route "/how-was-your-day"
def ask_day():  # Function to handle requests at "/how-was-your-day"
    return "<h1>How was your day?</h1>"  # Returning an HTML response

@app.route("/test")  # Defining the route "/test"
def test():  # Function to handle requests at "/test"
    data = request.args.get('x')  # Retrieving the 'x' parameter from the URL query string
    return "This is a data input for my url {}".format(data)  # Returning the extracted data in response

if __name__ == "__main__":  # Ensuring the script runs only when executed directly
    app.run(debug=True, host="0.0.0.0", port=5003)  # Running the Flask application with debugging enabled on port 5003


# To give the input first go to url- http://127.0.0.1:5003/test and then 
# modify the url as- http://127.0.0.1:5003/test?x=My name is Vivek singh  and now refresh the page 