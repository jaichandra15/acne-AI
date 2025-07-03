from flask import Blueprint, request, jsonify
from models.vertex_endpoint import classify_image

classify_bp = Blueprint("classify", __name__)

@classify_bp.route("/classify", methods=["POST"])
def classify():
    if "image" not in request.files:
        return jsonify({"error": "Image file is required"}), 400

    image_file = request.files["image"]
    image_bytes = image_file.read()
    print("Received image for classification")

    try:
        prediction = classify_image(image_bytes)
        return jsonify(prediction)
    except Exception as e:
        print(f"Error during classification: {e}")
        return jsonify({"error": str(e)}), 500
