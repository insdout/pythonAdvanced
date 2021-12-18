import argparse
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


def build_cli(args):
    inv_index = build_inverted_index(load_document(args.dataset))
    inv_index.dump(args.index)


def query_cli(args):
    inv_index = InvertedIndex.load(args.index)
    with open(args.query_file, "r") as f:
        for line in f:
            print(
                *sorted(
                    list(
                        inv_index.query(line.split())
                    )
                ), sep=",")


parser = argparse.ArgumentParser(description='CLI build/query')
subparsers = parser.add_subparsers(dest="command",
                                   help='type of command: [build, query]')

b_parser = subparsers.add_parser("build", help='arguments: [dataset, index]')
q_parser = subparsers.add_parser("query", help='arguments: [index,query_file]')

b_parser.add_argument("--dataset", type=str, required=True,
                      help='path to dataset')
b_parser.add_argument("--index", type=str, required=True,
                      help='path to dictionary')
b_parser.set_defaults(func=build_cli)
q_parser.add_argument("--index", type=str, required=True,
                      help='path to dictionary')
q_parser.add_argument("--query_file", type=str, required=True,
                      help='path to query file')
q_parser.set_defaults(func=query_cli)

args_parsed = parser.parse_args()
args_parsed.func(args_parsed)
