# MAIN API Server
from flask import Flask, request, jsonify
import json
import time
import os
from datetime import datetime

app = Flask(__name__)

# Path to the dataset map JSON
DATA_PATH = 'datasets'
SCRIPTS_PATH = 'scripts'
UTILS_PATH = 'utils'
METADATA_PATH = 'metadata.json'
CACHE_PATH = 'cache.json'
LOGS_PATH = 'logs/orchestrator.log'

# Load mapping from cache
def load_cache():
    '''Cache JSON: "path": what we need '''
    if os.path.exists(CACHE_PATH):
        with open(CACHE_PATH, 'r') as f:
            return json.load(f)
    return {}

# Load data map from memory
def load_memory(dataset):
    if os.path.exists(DATA_PATH+f"/{dataset}"):
        with open(DATA_PATH, 'r') as f:
            return json.load(f)
    return {}

@app.route('/dispatch', methods=['GET'])
def dispatch():
    filepath = request.args.get('filepath')
    cart = request.args.get('cart-id')
    location = request.args.get('zone')
    # do some sanitization / validity checks here

    print("DISPATCHED CART")

    return jsonify({
        "status": "success",
        "dataset": filepath,
        "cart": cart-id,
        "zone": location
    })

# Can do 2 things: simply fetches carts/locations OR calls dispatch
@app.route('/fetch', methods=['GET'])
def fetch():
    filepath = request.args.get('filepath')
    fetched_data = load_cache()

    if filepath not in fetched_data:
        fetched_data = load_memory(filepath)

    # TODO: do one more check here to ensure valid data found

    data_map = fetched_data[filepath]
    carts = data_map["carts"]

    return jsonify({
        "status": "success",
        "dataset": filepath,
        "carts": carts
    })

# @app.route('/store_data', methods=['POST'])
# @app.route('/create_data', methods=['POST'])

if __name__ == '__main__':
    # Create folders if they don't exist
    if not os.path.exists('datasets/'):
        exit(1)

    # open port 8080, over HTTP for simplicity reasons
    app.run(port=8080, debug=True)
