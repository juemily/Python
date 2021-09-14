from flask import Flask
from routes.pi import app_pi
from routes.auth import routes_auth
from dotenv import load_dotenv

app = Flask(__name__)

app.register_blueprint(routes_auth, url_prefix="")
app.register_blueprint(app_pi, url_prefix="")

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True, port=4000)
