import os 
from dotenv import load_dotenv
import requests
import numpy as np

from sentence_transformers import SentenceTransformer

model_id = "sentence-transformers/all-MiniLM-L6-v2"

load_dotenv()

hf_token = os.getenv("API_KEY")



model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

texts = ["How do I get a replacement Medicare card?",
        "What is the monthly premium for Medicare Part B?",
        "How do I terminate my Medicare Part B (medical insurance)?",
        "How do I sign up for Medicare?",
        "Can I sign up for Medicare Part B if I am working and have health insurance through an employer?",
        "How do I sign up for Medicare Part B if I already have Part A?",
        "What are Medicare late enrollment penalties?",
        "What is Medicare and who can get it?",
        "How can I get help with my Medicare Part A and Part B premiums?",
        "What are the different parts of Medicare?",
        "Will my Medicare premiums be higher because of my higher income?",
        "What is TRICARE ?",
        "Should I sign up for Medicare Part B if I have Veterans' Benefits?"]




question = "what three thing did i ask about"

q_embedding = model.encode(question)
db_embedding = model.encode(texts)


from sentence_transformers.util import semantic_search

dicts = semantic_search(q_embedding,db_embedding, top_k=5)
for dict in dicts[0]:
    print(texts[dict["corpus_id"]])
