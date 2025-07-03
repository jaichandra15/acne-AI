import os
import io
import base64
from dotenv import load_dotenv
from gradio_client import Client
from PIL import Image
import requests

def classify_image(image_bytes):
    load_dotenv()
    HF_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

    client = Client("RihemXX/Acnes", hf_token=HF_TOKEN)
    try:
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    except Exception as e:
        raise ValueError(f"Failed to open image: {e}")


    result = client.predict(
        image,
        api_name="/predict"
    )
    print("Model output:", result)

    # result[0]: image object with dict info
    # result[1]: severity string
    if isinstance(result, (tuple, list)) and isinstance(result[0], dict):
        image_dict = result[0]
        severity = result[1]

        # Get image content: try local path first, then fallback to URL
        # if image_dict.get("path"):
        #     with open(image_dict["path"], "rb") as f:
        #         img_data = f.read()
        # elif image_dict.get("url"):
        #     img_data = requests.get(image_dict["url"]).content
        # else:
        #     return {"error": "Image output not found"}

        # img_base64 = base64.b64encode(img_data).decode("utf-8")

        return {
            "severity": severity
        }

    return {"error": "Invalid model output"}
