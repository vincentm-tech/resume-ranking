# Dataset: https://www.kaggle.com/datasets/youssefkhalil/resumes-images-datasets

from paddleocr import PaddleOCR
import spacy
import re
import os
import ollama

class ResumeProcessor:
    def __init__(self, resume_folder, keywords_file):
        """Initialize OCR, NLP model, and load keywords."""
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en', show_log=False)
        self.nlp = spacy.load('en_core_web_sm')
        self.resume_folder = resume_folder
        self.keywords = self.load_keywords(keywords_file)

    def load_keywords(self, keywords_file):
        """Load keywords from a file into a set for faster lookup."""
        with open(keywords_file, "r") as file:
            return {line.strip().lower() for line in file if line.strip()}

    def iterate_files(self):
        """Return a list of all file paths in the resume folder."""
        return [os.path.join(self.resume_folder, f) for f in os.listdir(self.resume_folder) if os.path.isfile(os.path.join(self.resume_folder, f))]

    def extract_text(self, image_path):
        """Extract text from an image using OCR."""
        results = self.ocr.ocr(image_path, cls=True)
        return [entry[1][0] for entry in results[0]]  # List of extracted text lines

    def extract_candidate_info(self, image_path):
        """Extract the candidate's name using NLP entity recognition."""
        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        phone_pattern = r"(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})"
        results = self.ocr.ocr(image_path, cls=True)

        text_data = " ".join([entry[1][0] for entry in results[0]])

        email = re.findall(email_pattern, text_data)
        phone = re.findall(phone_pattern, text_data)

        for line in results[0]:
            text = line[1][0]
            doc = self.nlp(text)

            for entity in doc.ents:
                if entity.label_ == "PERSON":
                    clean_name = re.sub(r"\d+", "", entity.text).strip()
                    return clean_name, email[0], phone[0]  # Return first detected name
        return "Unknown", "Unknown", "Unknown"
    
    def AI_analysis(self, image_path):
        """Anlyze candidates stregnths using AI."""
        job_title = "Python Developer"  # Job title to analyze for
        results = self.ocr.ocr(image_path, cls=True)

        text_data = " ".join([entry[1][0] for entry in results[0]])

        prompt = f"Analyze this resume and identify the candidate's strengths for {job_title}:\n\n{text_data}"
        response = ollama.chat(model='mistral', messages=[{'role': 'user', 'content': prompt}])
        return response['message']['content']
    
    def rank_resume(self, resume_text):
        """Rank the resume based on keyword matches."""
        matches = set()

        for phrase in resume_text:
            phrase = phrase.lower()
            for keyword in self.keywords:
                if keyword in phrase:
                    matches.add(keyword)

        match_count = len(matches)
        keywords_count = len(self.keywords)

        percentage_match = (match_count / keywords_count) * 100 if keywords_count > 0 else 0
        return matches, percentage_match

    def process_resumes(self):
        """Process all resumes in the folder and rank them."""
        resume_files = self.iterate_files()
        applicant_results = []  # Store results for sorting
        resume_files = list(self.iterate_files())  # Convert generator to list
        total_resumes = len(resume_files)

        print(f"Processing {total_resumes} resumes...")
        for index, file in enumerate(resume_files, start=1):
            resume_text = self.extract_text(file)
            name, email, phone = self.extract_candidate_info(file)
            analysis = self.AI_analysis(file)
            matched_keywords, percentage_match = self.rank_resume(resume_text)

            # Calculate progress percentage
            progress = (index / total_resumes) * 100
            print(f"Progress: {progress:.2f}% ({index}/{total_resumes} resumes processed)")
            # Store in list for sorting
            applicant_results.append((name, email, phone, file, matched_keywords, percentage_match, analysis))

        # Sort by percentage_match in descending order
        applicant_results.sort(key=lambda x: x[5], reverse=True)

        # Print the sorted results
        print("\nFinal Ranked Resumes:\n" + "-" * 40)
        for rank, (name, email, phone, file, matched_keywords, percentage_match, analysis) in enumerate(applicant_results, start=1):
            print(f"Rank #{rank}")
            print(f"Candidate: {name} | Email: {email} | Phone: {phone}")
            print(f"File: {file}")
            print(f"Matched Keywords: {matched_keywords}")
            print(f"Score: {percentage_match:.2f}%")
            print("AI Analysis:\n", analysis)
            print("-" * 40)



# Example Usage
if __name__ == "__main__":
    processor = ResumeProcessor(resume_folder="resume_datasets", keywords_file="keywords.txt")
    processor.process_resumes()
