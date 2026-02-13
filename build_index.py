from sentence_transformers import SentenceTransformer
import faiss, numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("medical_data.txt","r",encoding="utf-8") as f:
    docs=[line.strip() for line in f if line.strip()]

embeddings=model.encode(docs)

index=faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

faiss.write_index(index,"index.faiss")
np.save("docs.npy",np.array(docs))

print("Index ready")
