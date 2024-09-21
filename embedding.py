import os
import json
from openai import OpenAI
from numpy import dot
from numpy.linalg import norm
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response.data[0].embedding

class EmbedItem:
    def __init__(self, text):
        self.text = text
        self.embedding = get_embedding(text)

class ComparisonResult:
    def __init__(self, text, similarity):
        self.text = text
        self.similarity = similarity

def calculate_similarity(a, b):
    return dot(a, b) / (norm(a) * norm(b))

# Build the list of embeddings to compare
items = []

# Try different encodings
encodings = ['utf-8', 'latin-1', 'cp1252']

for encoding in encodings:
    try:
        with open("e:/amazoncode/labs/embedding/items.txt", "r", encoding=encoding) as f:
            text_items = f.read().splitlines()
        break  # If successful, exit the loop
    except UnicodeDecodeError:
        continue  # If unsuccessful, try the next encoding
else:
    raise ValueError("Unable to decode the file with the attempted encodings")

for text in text_items:
    items.append(EmbedItem(text))

# Compare embeddings
for e1 in items:
    print(f"Closest matches for '{e1.text}'")
    print("----------------")
    cosine_comparisons = []
    
    for e2 in items:
        similarity_score = calculate_similarity(e1.embedding, e2.embedding)
        
        cosine_comparisons.append(ComparisonResult(e2.text, similarity_score))
        
    cosine_comparisons.sort(key=lambda x: x.similarity, reverse=True)
    
    for c in cosine_comparisons:
        print("%.6f" % c.similarity, "\t", c.text)
    
    print()