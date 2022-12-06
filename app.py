from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_my_ip():
    ip_addr = request.remote_addr
    return '<h1> You are connecting from:' + ip_addr
 #   return jsonify({'ip': request.remote_addr}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
