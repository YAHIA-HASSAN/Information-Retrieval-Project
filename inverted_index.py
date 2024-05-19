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
                documents.append(file.read())
                filenames.append(filename)
    return documents, filenames


# Function to tokenize text
def processing(text):
    return queryPreprocessing(text)


# Function to build an inverted index
def build_inverted_index(documents):
    inverted_index = defaultdict(list)
    for idx, doc in enumerate(documents):
        words = processing(doc)
        for word in words:
            if idx not in inverted_index[word]:
                inverted_index[word].append(idx)
    return inverted_index


# Function to rank documents based on the inverted index and query
def rank_documents(query, inverted_index):
    query_terms = processing(query)
    doc_scores = defaultdict(int)

    for term in query_terms:
        if term in inverted_index:
            for doc_idx in inverted_index[term]:
                doc_scores[doc_idx] += 1

    sorted_docs = sorted(doc_scores.items(), key=lambda x: x[1], reverse=True)
    top_docs = [doc_idx for doc_idx, score in sorted_docs[:10]]

    return top_docs


# Specify the directory containing your documents
directory = os.path.dirname(os.path.realpath(__file__)) + '\\Preprocessed\\'

# Read documents from files in the directory
docs, filenames = read_documents_from_directory(directory)

# Build the inverted index
inverted_index = build_inverted_index(docs)


# Function to process a query and retrieve top 10 document names
def retrieve_top_document_names(query):
    top_doc_indices = rank_documents(query, inverted_index)
    top_doc_names = [filenames[idx] for idx in top_doc_indices]
    return top_doc_names
