from transformers import pipeline
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

generator = pipeline('text-generation', model='gpt2')

app = FastAPI()


class Body(BaseModel):
    text: str


@app.get('/')
def root():
    return HTMLResponse("<h1>A self-documenting API to interact with a GPT2 model and generate text.</h1><p>Updated by givenfly 24 dec 2024</p>")


@app.post('/generate')
def predict(body: Body):
    results = generator(body.text, max_length=35, num_return_sequences=1)
    return results[0]
