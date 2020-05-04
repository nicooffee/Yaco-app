from flask import Flask
app = Flask(__name__)
#sdkjgfdskg
#sdkjgfdskg
#sdkjgfdskg
@app.route('/')
def hello_world():
    return "chao ola"

@app.route('/aaaa')
def aaa():
    return "gfkdjdfg"


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')