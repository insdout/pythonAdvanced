class CountVectorizer:
    def __init__(self, ngram_size):
        self.ngram_size = ngram_size
        self.vocabulary = {}

    def fit(self, corpus):
        self.vocabulary = {}
        tokens = set()
        for text in corpus:
            tokens.update(
                set(
                    [text[i: i+self.ngram_size]
                     for i in range(len(text)-self.ngram_size+1)]
                )
            )
        self.vocabulary.update(
            {(key, index) for index, key in enumerate(sorted(tokens))}
        )

    def transform(self, corpus):
        transformed = []
        for text in corpus:
            counter = [0] * len(self.vocabulary.keys())
            tokens = [
                text[i: i+self.ngram_size]
                for i in range(len(text)-self.ngram_size+1)
            ]
            for token in tokens:
                try:
                    token_index = self.vocabulary[token]
                    counter[token_index] += 1
                except KeyError:
                    continue
            transformed.append(counter)
        return transformed

    def fit_transform(self, corpus):
        self.fit(corpus)
        transformed = self.transform(corpus)
        return transformed
