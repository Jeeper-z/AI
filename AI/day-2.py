

from transformers import pipeline

generator = pipeline("text-generation",model="gpt2")
output = generator("Artificial Intelligence will",max_length=40)
print(output[0]["generated_text"])