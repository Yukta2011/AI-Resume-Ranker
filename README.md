AI-Powered Resume Ranker

This project ranks resumes based on their relevance to a given job description using Natural Language Processing (NLP). It supports PDF resume uploads, processes and scores them using TF-IDF and cosine similarity, and presents ranked results through a clean, user-friendly web interface built with Flask and styled using CSS.


 Features:

- 📄 Extract text from PDF resumes
- 🧠 Preprocess text using SpaCy (lemmatization, stopword removal)
- 📊 Vectorize text using TF-IDF
- 🎯 Score and rank resumes by similarity to job description
- 🌐 Web-based interface with file upload
- 📥 Downloadable HR report (CSV format)
- 🎨 Custom CSS styling for a clean and responsive UI


  Tech Stack:

| Tool         | Purpose                               |
|--------------|----------------------------------------|
| Python       | Core language                          |
| Flask        | Web app framework                      |
| SpaCy        | NLP preprocessing                      |
| Scikit-learn | TF-IDF vectorization & similarity      |
| PyMuPDF      | PDF text extraction                    |
| Pandas       | HR report generation                   |
| HTML/CSS     | Frontend UI styling                    |


 Project Structure:
AI-Resume-Ranker/
├── app.py
├── pdf_reader.py
├── scoring.py
├── text_preprocessing.py
├── static/
│ └── style.css
├── templates/
│ └── index.html
├── uploads/ # Stores uploaded resumes
├── requirements.txt
└── README.md

