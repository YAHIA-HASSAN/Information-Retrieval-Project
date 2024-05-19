from preprocessing import process
from term_document_matrix import retrieve_top_document_names
import os


def preprocess():
    process(os.path.dirname(__file__) + '\\Dataset\\',
            os.path.dirname(__file__) + '\\Preprocessed\\')


# Term document matrix usage:
def term_document_matrix(query):
    top_doc_names = retrieve_top_document_names(query)

    for idx, doc_name in enumerate(top_doc_names):
        print(f"Top Document {idx + 1}: {doc_name}")


def inverted_index(query):
    pass


def TF_IDF(query):
    pass


if __name__ == '__main__':
    # preprocess()
    ch = input("Select Retrieving Algorithm:\n"
               "1. Term Document Matrix\n"
               "2. Inverted Index\n"
               "3. TF/IDF\n")
    query = input("\n---------------------\n"
                  "Enter Query: ")
    if ch == "1":
        term_document_matrix(query)
    elif ch == "2":
        inverted_index(query)
    elif ch == "3":
        TF_IDF(query)
    else:
        print("Invalid Selected Algorithm")
