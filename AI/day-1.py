

from transformers import pipeline

classifer = pipeline("senttiment-analysis")
result = classifier("i love eating ice-cream in coorg")
print(result)