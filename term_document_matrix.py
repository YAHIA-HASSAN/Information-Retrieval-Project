import os
from collections import defaultdict
from preprocessing import queryPreprocessing


# Function to read documents from files in a directory
def read_documents_from_directory(directory):
    documents = []
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):  # Assuming text files
            with open(os.path.join(directory, filename), "r") as file:
                documents.append(file.read().split())
                filenames.append(filename)
    return documents, filenames


# Specify the directory containing your documents
directory = os.path.dirname(os.path.realpath(__file__)) + '\\Preprocessed\\'

# Read documents from files in the directory
docs, filenames = read_documents_from_directory(directory)


# Function to tokenize text
def processing(text):
    return queryPreprocessing(text)


# Function to compute term frequency
def compute_term_frequency(terms):
    term_freq = defaultdict(int)
    words = docs
    for word in words:
        if word in terms:
            term_freq[word] += 1
    return term_freq


# Function to rank documents based on query
def rank_documents(query):
    query_terms = processing(query)
    doc_scores = []

    for idx, doc in enumerate(docs):
        term_freq = compute_term_frequency(query_terms)
        score = sum(term_freq[term] for term in query_terms)
        doc_scores.append((score, idx))

    doc_scores.sort(reverse=True, key=lambda x: x[0])
    top_docs = [idx for score, idx in doc_scores[:10]]

    return top_docs


# Function to process a query and retrieve top 10 document names
def retrieve_top_document_names(query):
    top_doc_indices = rank_documents(query)
    top_doc_names = [filenames[idx] for idx in top_doc_indices]
    return top_doc_names
