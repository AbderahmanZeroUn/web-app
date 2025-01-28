from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define a route
@app.route('/')
def home():
    return "Hello from Docker!! This is a simple Flask app."

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
