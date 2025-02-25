# from fastapi import FastAPI
# from pydantic import BaseModel
# import torch
# from transformers import pipeline

# app = FastAPI()

# # Load AI Model (Example: Sentiment Analysis)
# nlp_model = pipeline("sentiment-analysis")

# class InputData(BaseModel):
#     text: str

# @app.post("/analyze")
# def analyze_text(data: InputData):
#     result = nlp_model(data.text)
#     return {"sentiment": result[0]["label"], "confidence": result[0]["score"]}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)


from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()
nlp_model = pipeline("sentiment-analysis")

@app.get("/")
def read_root():
    return {"message": "AI Agent Backend is Running!"}

@app.post("/analyze/")
def analyze_text(data: dict):
    text = data.get("text", "")
    if not text:
        return {"error": "No text provided"}
    result = nlp_model(text)
    return {"sentiment": result}
