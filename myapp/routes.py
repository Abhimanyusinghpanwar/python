from flask import Blueprint, jsonify
import logging

myapp_bp = Blueprint('myapp', __name__)

@myapp_bp.route('/health', methods=['GET'])
def health_check():
    logging.debug("Health check endpoint called")
    return jsonify({'status': 'healthy'}), 200

@myapp_bp.route('/greet/<name>', methods=['GET'])
def greet(name):
    logging.info(f"Greet endpoint called with name: {name}")
    return jsonify({'message': f'Hello, {name}! Welcome to Flask starter app.'}), 200
