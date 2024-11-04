from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello, Vercel!"  # Simple response for testing

def handler(req):
    with app.app_context():
        return app.full_dispatch_request()

if __name__ == '__main__':
    app.run(debug=True)