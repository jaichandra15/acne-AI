from flask import Blueprint, request, jsonify
from models.nlp_agent.langchain_wrapper import get_recommendation
from utils.prompt_builder import build_prompt

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.json
    prompt = build_prompt(data["severity"], data.get("medication"))
    reply = get_recommendation(prompt)
    return jsonify({"response": reply})