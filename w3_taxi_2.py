emp = input().split()
dict_emp = dict(
    map(
        lambda x: (x[1], x[0]),
        zip(
            range(len(emp)), map(int, emp))
    )
)
tax = input().split()
dict_tax = dict(
    map(
        lambda x: (x[1], x[0]),
        zip(
            range(len(tax)), map(int, tax))
    )
)

print(
    *map(
        lambda x: x[1],
        sorted(
            map(
                lambda x: (dict_emp[x[0]], dict_tax[x[1]]),
                zip(
                    sorted(
                        dict_emp, reverse=True
                    ),
                    sorted(
                        dict_tax,  reverse=False
                    )
                )
            )
        )
    )
)

print( *zip(sorted(enumerate(map(int,emp))),sorted(enumerate(map(int,tax)))))