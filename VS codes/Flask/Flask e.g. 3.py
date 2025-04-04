# if we want different URL for different functions
from flask import Flask  # Importing the Flask module to create a web application

app = Flask(__name__)  # Creating an instance of the Flask class for the web application

@app.route("/")  # Defining the route for the root URL ("/")
def greet():  # Function to handle requests to the root URL
    return """ 
        <h1>Hello, Everyone!</h1>  
        <h1>How are you?</h1>  
        <h1>How was your day?</h1>
    """  # Returning all responses in one HTML response

if __name__ == "__main__":  # Ensuring the script runs only if executed directly
    app.run(host="0.0.0.0", port=5002)  # Running the Flask application and making it accessible to all network interfaces in port port=5002

# Now, we can access all function at once by using one URL http://127.0.0.1:5002 or http://192.168.81.115:5002