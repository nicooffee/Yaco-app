from flask import Flask
from principal.Principal import principal
app = Flask(__name__)

app.register_blueprint(principal)



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')