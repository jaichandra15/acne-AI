import streamlit as st
import requests
import base64
from PIL import Image
import io



st.title("Acne Care Assistant")
image = st.file_uploader("Upload an acne image", type=["jpg", "png"])
prescription = st.file_uploader("Upload your prescription (optional)", type=["pdf", "png"])

if st.button("Analyze"):
    if image:
        res = requests.post("http://localhost:8000/classify", files={"image": image})
        print(res)
        severity = res.json()["severity"]
    else:
        severity = "mild"

    if prescription:
        text = requests.post("http://localhost:8000/prescribe", files={"prescription": prescription}).json()["text"]
    else:
        text = None

    reply = requests.post("http://localhost:8000/chat", json={"severity": severity, "medication": text})
    
    st.write(reply.json()["response"])
    if "mask_image" in reply:
        st.image(Image.open(io.BytesIO(base64.b64decode(reply["mask_image"]))), caption="Acne Region Segmentation")