from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

app = FastAPI()

# Load pre-trained GPT-2 model and tokenizer from Hugging Face
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Define the request model
class TextGenerationRequest(BaseModel):
    prompt: str
    max_length: int = 50

# Define the response model
class TextGenerationResponse(BaseModel):
    generated_text: str

@app.get("/")
def read_root():
    return {"message": "LLM API is running"}

@app.post("/generate-text", response_model=TextGenerationResponse)
def generate_text(request: TextGenerationRequest):
    try:
        # Encode the input prompt
        inputs = tokenizer.encode(request.prompt, return_tensors="pt")

        # Generate text using the model
        outputs = model.generate(inputs, max_length=request.max_length, num_return_sequences=1, no_repeat_ngram_size=2, early_stopping=True)

        # Decode the generated text
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return TextGenerationResponse(generated_text=generated_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

