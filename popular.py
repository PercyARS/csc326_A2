__author__ = 'zhaopeix'

from collections import defaultdict


def find_popular(file_name):
    # use defaultdict to create a dictionary with 0 as value
    d = defaultdict(lambda: 0)
    with open(file_name) as _file:
        for word in _file:
            d[word]+=1
    # return the top 10 counts
    top_10_sorted_count = sorted(list(set(d.values())))[::-1][:10]
    counter = 0
    for count in top_10_sorted_count:
        for key, value in d.items():
            if value == count:
                # remove the empty line trailing every key
                key = key.rstrip('\n')
                print "%s %d"% (key, value)
                counter += 1
                # since we only need 10
                if counter == 10:
                    return

find_popular("text")