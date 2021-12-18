words = input().split()
scores = input().split()
word_dict = dict(
    map(
        lambda z: (z[0], z[1]),
        filter(
            lambda x: x[1] > 0.5, zip(
                words,
                map(
                    float, scores
                )
            )
        )
    )
)
print(*sorted(word_dict, key=lambda x: word_dict[x],
              reverse=True), sep="\n")
