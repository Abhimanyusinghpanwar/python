"""
Flask application for Optimum IDP.
This is a simple Flask API template created by Optimum IDP.
"""
import logging
import os
from flask import Flask, jsonify
 
# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
 
# Create Flask application
app = Flask(__name__)
 
# Configuration from environment variables
PORT = int(os.environ.get('PORT', 5000))
ENV = os.environ.get('FLASK_ENV', 'development')
 
 
@app.route('/')
def hello_world():
    """
    Root endpoint that returns a welcome message.
    """
    logger.info('Python Flask App created by Optimum IDP')
    return jsonify({
        'message': 'Python Flask App created by Optimum IDP!',
        'status': 'success'
    })
 
 
@app.route('/health')
def health_check():
    """
    Health check endpoint for monitoring.
    Returns the current health status of the application.
    """
    logger.info('Health check endpoint was called')
    return jsonify({
        'status': 'healthy'
    })
 
 
if __name__ == '__main__':
    logger.info('Starting Flask app in %s mode', ENV)
    # When running directly, use Flask's built-in server
    app.run(host='0.0.0.0', port=PORT, debug=ENV == 'development')
else:
    # For Gunicorn, this will be the entry point
    logger.info('Flask app initialized for Gunicorn in %s mode', ENV)
    # Gunicorn will look for the 'app' variable
 

