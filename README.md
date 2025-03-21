# 📄 Resume Ranking System

## 🚀 Overview

This project is an AI-powered resume ranking system that extracts text from image-based resumes, analyzes candidate strengths, and ranks resumes based on keyword matches.

It leverages OCR (PaddleOCR), NLP (spaCy), and AI (Mistral LLM) to automate and enhance the resume screening process.

🔹 **Dataset Used**: [Resumes Images Dataset](https://www.kaggle.com/datasets/youssefkhalil/resumes-images-datasets)

## ✨ Features

✅ Extract text from image-based resumes using PaddleOCR

✅ Identify candidate names, emails, and phone numbers using NLP

✅ Analyze candidate strengths using Mistral AI

✅ Rank resumes based on keyword matches

✅ Process multiple resumes and generate ranked results

## 🛠️ Technologies Used

- 🐍 Python

- 🖼️ PaddleOCR (Optical Character Recognition)

- 🧠 spaCy (Natural Language Processing)

- 🔍 Regular Expressions (Regex) for email and phone extraction

- 🤖 Ollama (Mistral AI for resume analysis)

- 📂 OS module for file handling

## 📥 Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/resume-ranking-system.git
   cd resume-ranking-system
   ```

2. Install dependencies:
   ```sh
   pip install paddleocr spacy ollama
   ```

3. Download the English NLP model for spaCy:
   ```sh
   python -m spacy download en_core_web_sm
   ```

4. Ensure you have a folder named `resume_datasets` containing image-based resumes.

5. Create a `keywords.txt` file with a list of job-related keywords.

## ▶️ Usage

Run the script to process resumes:
```sh
python resume_processor.py
```

## 🔍 How It Works

1. The script loads keywords from `keywords.txt`.

2. It scans the `resume_datasets` folder for resumes.

3. Each resume is processed using OCR to extract text.

4. NLP techniques identify the candidate's name, email, and phone number.

5. AI analysis provides insights on the candidate's strengths.

6. Resumes are ranked based on keyword matches and AI evaluation.

7. The final ranked resumes are displayed in the console.

## 📊 Output

The script displays ranked resumes with:

- 👤 Candidate Name, Email, and Phone Number

- 📁 File Path

- 🔑 Matched Keywords

- 🎯 Score (percentage match)

- 🤖 AI Analysis of candidate strengths

## 🔮 Future Enhancements

🚀 **API Integration** - Build a REST API for remote access to resume ranking results.

⚡ **Reduce Processing Time** - Optimize OCR and NLP models for faster analysis.

📜 **Support for PDF Resumes** - Enable text extraction from PDF-based resumes.

📊 **Enhanced Ranking Metrics** - Implement AI-powered ranking based on job relevance.

🖥 **Web UI** - Develop an interactive dashboard for better visualization.

📂 **Export Results** - Save rankings to CSV, JSON, or database storage.

## 📜 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Vincent Manlesis

