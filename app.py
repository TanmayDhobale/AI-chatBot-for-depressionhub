from flask import Flask, render_template, request, jsonify
from chat import get_response

app = Flask(__name__)

@app.route("/")
def index_get():
    return render_template("base.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        text = data.get("message")
        
        # TODO: Check if text is valid or not
        response = get_response(text)
        
        message = {"answer": response}
        return jsonify(message)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
