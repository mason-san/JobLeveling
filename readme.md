# 🤖 JobLevelling — AI-Powered Resume Matcher & Explainer

**“Smarter hiring. Stronger resumes. Now with reasons.”**

Job Leveling is a local-first, privacy-friendly resume screening app that ranks resumes against job descriptions using **semantic similarity** — then explains **why** each resume scored the way it did.

🔍 Upload any job description and a batch of candidate resumes, and Job Leveling:
- Scores each resume with a smart NLP model
- Picks the top candidates
- Asks a local LLM (DeepSeek via [Ollama](https://ollama.com)) to **explain the match**  
  > "This candidate matches due to Python, Flask, AWS; missing Docker and CI/CD."

This is resume screening — *with actual insight*.

---

## 💡 Features

- 📎 **Bulk Resume Uploads** — drop in all your PDFs
- 🧠 **AI-Powered Scoring** — SBERT + cosine similarity
- 📊 **Ranked Results Table** — scores, labels, and PDF previews
- 🧾 **Explainability Engine** — DeepSeek LLM explains *why* a resume matches
- 📥 **CSV Download** — export all scores and labels
- 🔒 **Local Only** — no API keys, no data leakage

---

## 🛠 Tech Stack

| Layer     | Tech                                 |
|-----------|--------------------------------------|
| Backend   | Python, Streamlit, Scikit-learn      |
| NLP Model | `all-MiniLM-L6-v2` (Sentence Transformers) |
| LLM       | `DeepSeek R1` via Ollama (local)     |
| PDF Parse | pdfplumber                           |
| Charts    | Matplotlib + Streamlit Charts        |

---

## 🚀 How to Run It Locally

### 📦 1. Install Requirements

```bash
pip install -r requirements.txt
