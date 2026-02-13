import faiss, numpy as np
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load LLM
model_name="google/flan-t5-base"
tokenizer=AutoTokenizer.from_pretrained(model_name)
llm=AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Load vector DB
index=faiss.read_index("index.faiss")
docs=np.load("docs.npy",allow_pickle=True)

def search(query,k=2):
    vec=embed_model.encode([query])
    D,I=index.search(np.array(vec),k)
    return [docs[i] for i in I[0]]

def generate_answer(context,question):
    prompt=f"""
You are a medical assistant. Give short safe answers.

Context:
{context}

Question:{question}
Answer:
"""
    inputs=tokenizer(prompt,return_tensors="pt",truncation=True)
    outputs=llm.generate(**inputs,max_new_tokens=120)
    return tokenizer.decode(outputs[0],skip_special_tokens=True)

def get_rag_answer(question):
    context="\n".join(search(question))
    return generate_answer(context,question)
