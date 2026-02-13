# 🩺 Healthcare FAQ RAG Chatbot – Project Documentation

## 1. Introduction

The Healthcare FAQ RAG Chatbot is a web-based application designed to answer basic medical questions using Artificial Intelligence.

The chatbot uses **Retrieval-Augmented Generation (RAG)** to provide accurate answers from a small medical knowledge base.

This project demonstrates how AI can be used in healthcare information systems.

---

## 2. Problem Statement

Many people search online for basic health information.
However, search engines often provide too much or unreliable information.

This project solves the problem by:

* Using a curated medical knowledge base
* Retrieving only relevant information
* Generating safe and short answers

---

## 3. Objectives

* Build a medical FAQ chatbot
* Implement RAG architecture
* Create a simple chatbot web interface
* Run fully on CPU (no GPU required)
* Make beginner-friendly AI project

---

## 4. Technologies Used

| Technology            | Purpose                      |
| --------------------- | ---------------------------- |
| Python                | Programming language         |
| Flask                 | Web framework                |
| Sentence Transformers | Convert text into embeddings |
| FAISS                 | Vector database for search   |
| Transformers          | AI text generation model     |
| HTML/CSS/JS           | Frontend interface           |

---

## 5. System Architecture

User → Flask Web App → RAG Engine →
Vector Search → LLM → Response → User

---

## 6. RAG Workflow

### Step 1: Data Preparation

Medical FAQ text is stored in `medical_data.txt`.

### Step 2: Embedding Creation

Sentence Transformer converts each sentence into vector form.

### Step 3: Vector Indexing

FAISS stores embeddings for fast similarity search.

### Step 4: Query Processing

User question is converted to vector and matched with stored data.

### Step 5: Answer Generation

FLAN-T5 model generates final response using retrieved context.

---

## 7. Features

* AI based chatbot
* Fast search using vector database
* Lightweight LLM
* Simple web UI
* Runs locally without cloud services

---

## 8. Advantages

* Low cost (no paid APIs)
* Beginner friendly
* Easy to extend with more data
* Real-world AI architecture

---

## 9. Limitations

* Not a replacement for doctors
* Small dataset
* Provides general medical guidance only

---

## 10. Future Enhancements

* Add larger medical dataset
* Add voice input
* Deploy online
* Add multilingual support

---

## 11. Conclusion

The project successfully demonstrates how RAG can be used to build a simple healthcare chatbot.

It provides a strong foundation for learning AI, NLP, and web development.
