from flask import Flask
from routes.classify import classify_bp
from routes.prescribe import prescribe_bp
from routes.chat import chat_bp

app = Flask(__name__)
app.register_blueprint(classify_bp)
app.register_blueprint(prescribe_bp)
app.register_blueprint(chat_bp)

if __name__ == "__main__":
    app.run(debug=True, port=8000)