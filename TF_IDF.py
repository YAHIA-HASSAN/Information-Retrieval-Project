import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Function to read documents from files in a directory
def read_documents_from_directory(directory):
    documents = []
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):  # Assuming text files
            with open(os.path.join(directory, filename), "r") as file:
                documents.append(file.read())
                filenames.append(filename)
    return documents, filenames


# Function to rank documents based on cosine similarity
def rank_documents(query, documents):
    # Create a TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()

    # Fit and transform the documents into TF-IDF vectors
    docs_tfidf = vectorizer.fit_transform(documents)

    # Transform the query into a TF-IDF vector
    query_tfidf = vectorizer.transform([query])

    # Compute cosine similarity between the query and all documents
    cosine_similarities = cosine_similarity(query_tfidf, docs_tfidf).flatten()

    # Get the indices of the top 10 documents sorted by similarity
    top_doc_indices = cosine_similarities.argsort()[-10:][::-1]

    return top_doc_indices


# Specify the directory containing your documents
directory = os.path.dirname(os.path.realpath(__file__)) + '\\Preprocessed\\'

# Read documents from files in the directory
docs, filenames = read_documents_from_directory(directory)


# Function to process a query and retrieve top 10 document names
def retrieve_top_document_names(query):
    top_doc_indices = rank_documents(query, docs)
    top_doc_names = [filenames[idx] for idx in top_doc_indices]
    return top_doc_names
