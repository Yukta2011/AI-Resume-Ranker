from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(resume_texts , job_description):
    #Combine JD with resumes
    documents = [job_description] + resume_texts
    # Instantiate the vectorizer
    vectorizer = TfidfVectorizer() 
    # Convert text to TF-IDF matrix
    tfidf_matrix = vectorizer.fit_transform(documents) 
    # Convert text to TF-IDF matrix
    scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten() #.flatten(): Converts the result from a 2D array to a 1D array of scores.
    
    return scores