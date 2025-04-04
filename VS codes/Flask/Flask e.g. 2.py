# if we want different URL for different functions

from flask import Flask  # Importing the Flask module to create a web application

app = Flask(__name__)  # Creating a Flask app instance

@app.route("/")  # Root URL "/"
def greet():
    return "<h1>Hello, Everyone</h1>"

@app.route("/how-are-you")  
def ask_well():
    return "<h1>How are you?</h1>"

@app.route("/how-was-your-day") 
def ask_day():
    return "<h1>How was your day?</h1>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)  # Debug mode enabled and another port port=5001 given
 
 # Now try accessing each function by http://127.0.0.1:5001 for Hello Everyone, 
                                    # http://127.0.0.1:5001/how-are-you for How are you? and
                                    # http://127.0.0.1:5001/how-was-your-day for How was your day?