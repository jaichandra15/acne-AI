from flask import Blueprint, request, jsonify
from utils.ocr_parser import parse_prescription

prescribe_bp = Blueprint("prescribe", __name__)

@prescribe_bp.route("/prescribe", methods=["POST"])
def prescribe():
    file = request.files["prescription"]
    parsed_text = parse_prescription(file.read())
    return jsonify({"text": parsed_text})