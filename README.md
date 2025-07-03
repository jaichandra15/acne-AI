# Acne Care Assistant 🤖💬🧴

A conversational AI-powered assistant that helps users manage acne-related concerns with compassion and clinical support. This application accepts acne photos for automated severity classification, optionally reads typed prescriptions, and provides personalized skincare advice and emotional support via a friendly chatbot interface.

🚀 Features

🧠 AI Chat Support: Powered by LangChain & GPT, the assistant answers queries like:

* “When should I apply this cream?”
* “How long before this medicine works?”
* “What diet should I follow for my acne type?”
* “I’m anxious about my acne. Any tips to feel better?”

📷 Acne Photo Classification:

* Upload acne images for severity detection (mild, moderate, severe)
* Visual segmentation of acne areas (powered by ViT & UNet model from rihem-bs02/Acnes)
* Returns severity label and overlaid skin segmentation mask

📄 Prescription Reading (Optional):

* Upload typed prescriptions
* Parsed using Google Cloud Document AI
* Extracts medicine names and instructions for enhanced recommendation accuracy

🌿 Home Remedies & Product Advice:

* Based on acne type and prescription
* Suggests affordable OTC products, home remedies, and do's & don'ts

❤️ Mental Health Support:

* Empathetic responses to boost user confidence
* AI acts as a positive, non-judgmental friend for teens and adults alike

🧰 Tech Stack

* Vertex AI (Google Cloud) – For acne image model deployment
* Document AI – For prescription OCR
* LangChain + OpenAI GPT – Conversational agent logic
* Flask – Backend API service
* Streamlit – Frontend interface
* Hugging Face Gradio Client – Optional fallback for public models
* Python, PIL, io, base64 – Image processing utilities

📂 Project Structure

acne-care-assistant/
├── frontend/             → Streamlit app UI<br>
├── backend/              → Flask server<br>
│   ├── routes/           → /classify, /prescribe, /chat APIs<br>
│   └── utils/            → image parser, prompt builder<br>
├── models/               → acne\_model (Vertex endpoint), langchain\_agent<br>
├── data/                 → Example inputs<br>
├── gcp\_config/           → Cloud deployment configs<br>
├── .env                  → API keys<br>
├── requirements.txt      → Dependencies<br>
└── README.md             → You're reading it.<br>

💻 How to Run Locally

1. Clone this repo:
   git clone [https://github.com/jaichandra15/acne-AI](https://github.com/jaichandra15/acne-AI)

2. Install dependencies:
   pip install -r requirements.txt

3. Set your API keys in a .env file:
   OPENAI\_API\_KEY=your-key
   HUGGINGFACE\_API\_KEY=your-key
   GOOGLE\_APPLICATION\_CREDENTIALS=path-to-your-gcp-key.json

4. Start Flask backend:
   cd backend
   python main.py

5. Start Streamlit app:
   cd frontend
   streamlit run app.py

🛠 Future Improvements

* Multilingual chat support for Indian regional languages
* Handwritten prescription OCR using LayoutLMv3 or Tesseract
* Secure login & privacy features (HIPAA, GDPR)
* Local model fallback (offline mode)

📬 Contributing

Pull requests are welcome! Please open an issue first to discuss major changes.

