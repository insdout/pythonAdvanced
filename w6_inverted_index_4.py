import pickle


class InvertedIndex:
    def __init__(self, word_to_docs_mapping):
        self.inverted_dic = word_to_docs_mapping

    def query(self, words):
        sets = [
            set(self.inverted_dic[word]) if word in self.inverted_dic
            else set() for word in words
        ]
        return set.intersection(*sets)

    def dump(self, filepath):
        with open(filepath, 'wb') as fp:
            pickle.dump(self, fp)

    @classmethod
    def load(cls, filepath):
        with open(filepath, 'rb') as fp:
            obj = pickle.load(fp)
        return obj


def build_inverted_index(articles):
    rev_dict = {}
    for _key in articles:
        for val in set(articles[_key].split()):
            rev_dict.setdefault(val, set()).update({_key})
    return InvertedIndex(rev_dict)


def load_document(filepath):
    dic = {}
    with open(filepath, mode="r", encoding="utf-8") as f:
        for line in f:
            _id, rest = line.split(sep="\t", maxsplit=1)
            dic.update({int(_id): rest.strip()})
    return dic
