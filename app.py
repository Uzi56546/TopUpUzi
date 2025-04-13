# Backend Flask sederhana
from flask import Flask, render_template, request, jsonify, send_from_directory
app = Flask(__name__)

orders = []
done_orders = []

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/submit-order', methods=['POST'])
def submit_order():
    data = request.json
    required_fields = ['game', 'id', 'jumlah', 'metode']
    if not all(field in data for field in required_fields):
        return jsonify({'status': 'error', 'message': 'Invalid data'}), 400

    # Simpan order ke database (contoh sederhana)
    order = {
        'game': data['game'],
        'id': data['id'],
        'jumlah': data['jumlah'],
        'metode': data['metode'],
        'pesan': data.get('pesan', '')
    }
    orders.append(order)
    return jsonify({'status': 'success', 'order': order})

@app.route('/orders')
def get_orders():
    return jsonify({'orders': orders, 'done': done_orders})

@app.route('/confirm-order', methods=['POST'])
def confirm_order():
    idx = request.json.get('index')
    if 0 <= idx < len(orders):
        done_orders.append(orders.pop(idx))
    return jsonify({'status': 'confirmed'})

@app.route('/cancel-order', methods=['POST'])
def cancel_order():
    idx = request.json.get('index')
    if 0 <= idx < len(orders):
        orders.pop(idx)
    return jsonify({'status': 'cancelled'})

if __name__ == '__main__':
    app.run(debug=True)
