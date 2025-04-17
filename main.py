from flask import Flask
from myapp.routes import myapp_bp
from config.config import Config
from logging.logger import setup_logger

app = Flask(__name__)
app.config.from_object(Config)

setup_logger()
app.register_blueprint(myapp_bp)

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, host='0.0.0.0', port=5000)

