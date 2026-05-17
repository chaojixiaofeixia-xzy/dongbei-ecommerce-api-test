from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 模拟东北特产数据（真实项目会用数据库）
products = [
    {"id": 1, "name": "五常大米", "price": 68.00, "stock": 100},
    {"id": 2, "name": "哈尔滨红肠", "price": 45.00, "stock": 200},
    {"id": 3, "name": "长白山人参", "price": 298.00, "stock": 50},
    {"id": 4, "name": "榛蘑", "price": 88.00, "stock": 80},
    {"id": 5, "name": "松子", "price": 55.00, "stock": 150},
]

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify({"code": 200, "data": products, "message": "success"})

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify({"code": 200, "data": product})
    return jsonify({"code": 404, "message": "商品不存在"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)