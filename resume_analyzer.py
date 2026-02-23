import nltk
import re
import numpy as np
import pandas as pd

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

nltk.download('stopwords')
nltk.download('wordnet')

# Sample Resume Data (Unstructured)

resumes = [
    "Experienced Data Analyst skilled in Python, Tableau, Data Visualization and SQL",
    "Machine Learning Engineer with Python, Deep Learning, NLP, and TensorFlow",
    "Web Developer proficient in HTML, CSS, JavaScript and React",
    "Software Tester with experience in manual testing and automation tools"
]

# Text Preprocessing Function

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z ]', '', text)
    words = text.split()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return " ".join(words)

cleaned_resumes = [preprocess_text(resume) for resume in resumes]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(cleaned_resumes)

# Contextual Clustering (KMeans)

kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X)

def calculate_score(tfidf_vector):
    score = tfidf_vector.sum()
    normalized_score = min(10, round(score * 10, 2))
    return normalized_score

scores = [calculate_score(X[i]) for i in range(X.shape[0])]

output = pd.DataFrame({
    "Resume_Text": resumes,
    "Cluster": clusters,
    "Score (0-10)": scores
})

print("\n===== Resume Analysis Result =====\n")
print(output)
