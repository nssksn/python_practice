from collections import defaultdict
from collections import Counter

def count_dict(string):
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1

    print(count_dict)


def count_characters(string):
    count_dict = defaultdict(int)
    for c in string:
        count_dict[c] += 1

    print(count_dict)

count_dict("Dynasty")
count_characters("Dynasty")
print(Counter("Dynasty"))
