def build_prompt(severity, medication=None):
    return f"""
    A user has {severity} acne.
    {f"They are using {medication}." if medication else ""}
    Recommend a skincare routine, suggest home remedies, and offer kind support.
    """