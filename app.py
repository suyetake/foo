from flask import Flask

app = Flask(__name__)

@app.route('/')  # example: 'http://www.google.com/'
                 # decorator endpoint for the home page,
                 # acting on the following method.
def home():
    return "Hello, world!"

app.run(port=5000)

# created and ran a simple flask application from Python.
# will consider how to use a REST API from within a JavaScript application

