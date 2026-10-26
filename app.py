from flask import Flask, jsonify, request

app = Flask(__name__)
items = []   # temporary storage in memory

@app.get("/")
def home():
    return jsonify(message="API is running")

@app.get("/items")
def list_items():
    return jsonify(items)

@app.post("/items")
def add_item():
    data = request.json
    if not data or "name" not in data:
        return jsonify(error="name is required"), 400
    items.append(data)
    return jsonify(data), 201

app.run(host="0.0.0.0", port=8080)