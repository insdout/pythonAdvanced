#file_path = r"C:\Users\mzaytsev\PycharmProjects\pythonAdvanced\wikipedia_sample.txt"
file_path = r"C:\Users\mzaytsev\PycharmProjects\pythonAdvanced\test.txt"
import re


class InvertedIndex:
    def __init__(self, word_to_docs_mapping):
        self.inverted_dic = word_to_docs_mapping

    def query(self, words):
        common_set = set.union(*self.inverted_dic.values())
        for word in words:
            if word in self.inverted_dic:
                common_set.intersection_update(set(self.inverted_dic[word]))
            else:
                common_set.intersection_update(set())
        return common_set


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
            max_len = max(map(len, re.findall(' +', rest[:50])))
            if max_len > 2:
                title, article = rest.split(sep="  ", maxsplit=1)
            else:
                title, article = rest.split(sep=" ", maxsplit=1)
            article = article.rstrip().lstrip()
            tit_art = title.rstrip().lstrip() + " " + article
            dic.update({int(_id): tit_art})

    return dic


d_dic = load_document(file_path)
II = build_inverted_index(load_document(file_path))
print(II.inverted_dic)
print("========")
print(d_dic)
print("========")
print(build_inverted_index(d_dic).inverted_dic)
print("========")
print("========")
print("queryis:")
queries =[['Python'],['Python', 'C++'], ['Java', 'is'] ,['is', 'a', 'general-purpose', 'programming', 'language']]
for _query in queries:
    print(_query, II.query(_query))
print("========")
d_test = {
    1: 'Python Python is an interpreted, high-level, general-purpose programming language',
    2: 'Java Java is a general-purpose programming language',
    3: 'C++ C++ is a high-level, general-purpose programming language',
}

for key in build_inverted_index(d_dic).inverted_dic:
    print(key,":",build_inverted_index(d_dic).inverted_dic[key])

print(build_inverted_index(d_dic).inverted_dic)
print(build_inverted_index(d_dic))

