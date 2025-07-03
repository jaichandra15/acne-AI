from google.cloud import documentai_v1 as documentai

def parse_prescription(file_bytes):
    client = documentai.DocumentUnderstandingServiceClient()
    document = documentai.types.Document.from_proto(file_bytes)
    return document.text