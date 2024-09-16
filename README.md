# Information-Retrieval-Project

## Overview
The **Information-Retrieval-Project** is a simple search engine implementation that demonstrates key algorithms used in information retrieval. This project covers the basics of indexing and searching using techniques like Word-document Matrix, Inverted Index, and TF/IDF (Term Frequency-Inverse Document Frequency). It can be used as an educational tool to understand the inner workings of search engines and how they retrieve relevant information from a corpus of documents.

## Features
- **Word-document Matrix**: Representation of the relationship between words and documents using a matrix.
- **Inverted Index**: Efficient data structure for mapping terms to their occurrences in a document collection.
- **TF/IDF**: Measures the importance of terms within a document relative to a corpus, improving the relevance of search results.

## Algorithms Implemented
1. **Word-document Matrix**  
   A matrix where rows represent documents and columns represent words. Each cell contains the frequency of a word in a specific document.
   
2. **Inverted Index**  
   A structure that maps words to the list of documents in which they appear. This allows for fast look-up of documents relevant to a search query.
   
3. **TF/IDF (Term Frequency-Inverse Document Frequency)**  
   A weighting scheme used to evaluate how important a word is in a document relative to the entire corpus. It improves search results by giving higher weight to distinctive terms in each document.
