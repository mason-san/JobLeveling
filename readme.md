# JobLevling – B2C MVP 🎓

> *“Is your resume job-ready? Find out in 30 seconds — with AI.”*

JobLeveling helps job seekers and students understand how well their resume matches a job description using AI-powered feedback.

This version is built for **students and early-career professionals** who want fast, actionable resume scoring — no downloads, no setup, no recruiter gatekeeping.

---

## ✨ Features

- ✅ Upload your resume (PDF)
- ✅ Paste a job description **or** select a preset template
- ✅ Get a match score (0–100%)
- ✅ See 3 strengths and 3 missing skills
- ✅ Receive a one-line AI summary
- ✅ Hosted on Streamlit Cloud
- ✅ Uses OpenAI (GPT-3.5 or GPT-4) for fast, intelligent feedback

---

## 🚀 Try It Now

> [🔗 Streamlit App Link](https://your-app-link.com)

---

## 🧠 How It Works

1. You upload your resume (PDF only).
2. Paste a job description or pick from our templates.
3. We compare the two using semantic similarity + GPT.
4. Get clear, readable feedback on how you match.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **AI Model:** OpenAI GPT-3.5-turbo or GPT-4
- **NLP:** Sentence Transformers for scoring (optional)
- **PDF Parsing:** pdfplumber

---

## 🔒 Privacy

- Your resume is not saved.
- Feedback is generated in real time and not stored.
- This version uses OpenAI’s API — enterprise/offline version is under development.

---

## 🛣️ Roadmap

- [ ] Add feedback history / save results
- [ ] Customize resume tips based on user goals
- [ ] Add “build your resume” AI tool
- [ ] Deploy public SaaS beta

---

## 🧪 Dev Setup (Optional)

```bash
git clone https://github.com/yourname/JobLeveling.git
cd JobLeveling 
git checkout b2c-mvp
pip install -r requirements.txt
streamlit run app.py
