from flask import flask

app = Flask(__name__)

@app.route('/example/')
def example():
    return {'hello': 'world'}

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
