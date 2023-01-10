from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class DocStats:
    def __init__(self, query, collection) -> None:
        self.query = query
        self.collection = collection


    def cosine_similarity(self) -> list:
        cur = self.collection.find({})
        data = [self.query]
        full_data = [None]

        for documents in cur:
            line = " ".join(documents["data"])
            data.append(line)
            full_data.append(documents)
        
        tfidfvectorizer = TfidfVectorizer(analyzer='word', stop_words='english')
        tfidf_wm = tfidfvectorizer.fit_transform(data)

        cosSim = cosine_similarity(tfidf_wm[0], tfidf_wm)
        sorted_cs = cosSim.argsort()

        links = []

        cur = self.collection.find({})
        
        for i in range(2, 20):
            links.append(full_data[sorted_cs[0][len(data) - i]]["url"])
        
        return links

