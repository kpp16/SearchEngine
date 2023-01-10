from stop_words import get_stop_words
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class WordProcessor:
    def __init__(self):
        self.stop_words = list(get_stop_words('en'))
        self.nltk_words = list(stopwords.words('english'))
        self.stop_words.extend(self.nltk_words)

    
    def process_doc(self, data):
        tokens = word_tokenize(data)
        filtered_line = [w for w in tokens if not w in self.stop_words]
        return filtered_line
