from fastapi import APIRouter, UploadFile, File
from model_loader import llm
from rag import query_docs
from prompts import SYSTEM_PROMPT, TEMPLATES
from security import redact

router = APIRouter()

@router.post("/chat")
async def chat(data: dict):
    task = data.get("task")
    prompt = data.get("prompt")

    if task in TEMPLATES:
        prompt = TEMPLATES[task].format(details=prompt, mos="92Y", award_type="ARCOM",
                                         subject="General", rank="SGT", name="Doe", topic=prompt)

    full_prompt = SYSTEM_PROMPT + "\n" + prompt
    result = llm(prompt=full_prompt, max_tokens=512)
    output = result["choices"][0]["text"]
    return {"response": redact(output)}

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    contents = await file.read()
    with open(f"data/uploads/{file.filename}", "wb") as f:
        f.write(contents)
    return {"status": "uploaded"}
