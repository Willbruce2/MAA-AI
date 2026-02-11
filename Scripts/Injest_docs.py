SYSTEM_PROMPT = """
You are MAA-AI, a Military Administration Assistant.
You assist with official writing, counseling, awards, evaluations, and training documents.
Use clear, professional military tone. Follow Army Values and doctrinal style.
If documents are provided, answer only using them.
"""

TEMPLATES = {
    "ncoer": "Write a strong NCOER bullet for MOS {mos} with achievements: {details}",
    "award": "Draft an {award_type} citation for a soldier with the following accomplishments: {details}",
    "mfr": "Write a Memorandum for Record on subject: {subject} with these details: {details}",
    "counseling": "Write a developmental counseling statement for {rank} {name} focusing on: {topic}",
}
