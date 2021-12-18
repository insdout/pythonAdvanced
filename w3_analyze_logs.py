import json
cant_read = 0
status_200 = 0
status_empty = 0
status_digit = 0
status_wrong_string = 0
file_name = input()
with open(file_name) as f0:
    for line in f0:
        try:
            log = json.loads(line)
        except json.decoder.JSONDecodeError as e:
            cant_read += 1
            continue
        if "status" in log.keys():
            try:
                status = log["status"]
                if status in {"", None}:
                    status_empty += 1
                    continue
                else:
                    if type(int(status)) == int:
                        if int(status) == 200:
                            status_200 += 1
                        else:
                            status_digit += 1
            except ValueError as v:
                status_wrong_string += 1
                continue
        else:
            status_empty += 1
print(
    status_200, status_digit,
    status_wrong_string, status_empty,
    cant_read,
    sep="\n"
)
