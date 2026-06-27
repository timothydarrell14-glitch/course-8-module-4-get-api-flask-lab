from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Home Page"

# TODO: Implement GET /products route that returns all products or filters by category

@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")
    if category:
        category = category.lower()
        filtered = [item for item in products if item["category"].lower() == category]
        return jsonify(filtered), 200
    return jsonify(products), 200

@app.route("/products/<int:id>")
def get_product_by_id(id):

    for p in products:
       if p["id"] == id:
          return jsonify(p), 200
    return jsonify({"message": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
