from fastapi import FastAPI
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForTokenClassification
from pydantic import BaseModel


class Item(BaseModel):
    text: str

app = FastAPI()
tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
nlp = pipeline("ner", model=model, tokenizer=tokenizer)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/recognition/")
def recognition(item: Item):
    return str(nlp(item.text))

