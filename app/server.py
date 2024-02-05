from flask import Blueprint, jsonify, request
from .database import *

server_blueprint = Blueprint('server', __name__)

@server_blueprint.route("/update", methods=['POST'])
def update():
    data = request.json

    params = {
        "ip_address" : request.remote_addr,
        "mac_address" : data['mac_address'],
        "status" : data['status'],
        "last_online" : data['last_online'],
    }

    count = check_primary_key(params)
    if count == 0:
        insert_client(params)
    else:
        update_client_status(params)

    return jsonify({"OK" : 200})


@server_blueprint.route("/status", methods=['GET'])
def status():
    clients = fetch_clients()
    return jsonify(clients), 200

