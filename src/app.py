from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [{"label": "My first task", "done":False}]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    if not request_body or "label" not in request_body:
        return jsonify({"error": "Invalid input"}), 400
    todos.append(request_body)
    print ("Incoming request with the following body", request_body)
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    try:
        del todos [position]
        print("This is the position o delete", position)
        return jsonify(todos), 200
    except IndexError:
        return jsonify({"error" : "Invalid position"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3245, debug=True)