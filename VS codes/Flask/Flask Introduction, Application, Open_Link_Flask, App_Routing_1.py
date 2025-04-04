# Flask Introduction, Application, Open_Link_Flask, App_Routing

from flask import Flask  # Importing the Flask module to create a web application

app = Flask(__name__)  # Creating an instance of the Flask class for the web application

@app.route("/")  # Defining the route for the root URL ("/")
def hello_everyone():  # Function to handle requests to the root URL
    return "<h1>Hello, Everyone<h1>"  # Returning an HTML heading as the response

if __name__ == "__main__":  # Ensuring the script runs only if executed directly
    app.run(host="0.0.0.0")  # Running the Flask application and making it accessible to all network interfaces
   

# if we want to access the function then go to the url got in output i.e.- http://192.168.81.115:5000 or http://127.0.0.1:5000