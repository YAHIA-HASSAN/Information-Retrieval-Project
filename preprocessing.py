import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
import os

def process(dataset_path, processed_dataset_path):
    stop_words = set(stopwords.words('english'))
    porter = PorterStemmer()
    if not os.path.exists(processed_dataset_path):
        os.makedirs(processed_dataset_path)

    list = os.listdir(dataset_path)
    all=len(list)
    for i in range(all):
        doc = open(dataset_path + list[i], 'r').read()
        words = word_tokenize(doc)
        filtered_sentence = [porter.stem(w) for w in words if
                             (w.lower() not in stop_words) and (w.lower() not in string.punctuation)]
        with open(processed_dataset_path + list[i], 'w') as filtered_file:
            filtered_file.write(' '.join(filtered_sentence))
        print(f'Processed-------<{(i/all)*100:.3f}%>-------<{list[i]}>')

