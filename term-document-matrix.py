import os
import numpy as np


# Function to read documents from files in a directory
def read_documents_from_directory(directory):
    documents = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):  # Assuming text files
            with open(os.path.join(directory, filename), "r") as file:
                documents.append(file.read())
    return documents


# Specify the directory containing your documents
directory = os.path.dirname(os.path.realpath(__file__)) + '\\Preprocessed\\'

# Read documents from files in the directory
docs = read_documents_from_directory(directory)
files_list = os.listdir(directory)

# Tokenize the documents
words_list = [doc.split() for doc in docs]

# Get unique terms (words)
unique_terms = sorted(set(word for doc in words_list for word in doc))

# Create term-document matrix
term_doc_matrix = {}

# Fill term-document matrix

for term in unique_terms:
    term_doc_matrix[term] = []

    for doc in docs:
        if term in doc:
            term_doc_matrix[term].append(True)
        else:
            term_doc_matrix[term].append(False)


# Display the term-document matrix
print("Term-Document Matrix:")
print(term_doc_matrix)
print()

# Display the terms
print("Terms:")
print(unique_terms)