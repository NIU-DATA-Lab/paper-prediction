from flask import Flask, request, jsonify, abort
app = Flask(__name__)

@app.route("/api/v1/predict", methods=["POST"])
def predict():
    response = flask.Response(
        status_code=202
    )
    response.headers["Location"] = "/api/v1/predict/9001"
    return response

@app.route("/api/v1/predict/<int:prediction_id>", methods=["GET"])
def results(prediction_id):
    if prediction_id == 9001:
        return jsonify(
            prediction_id="9001",
            policy={"prediction": True, "confidence": 0.5},
            public_understanding={"similarity_score": .75}
        )
    else:
        abort(404)
