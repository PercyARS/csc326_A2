__author__ = 'zhaopeix'

from collections import defaultdict

def find_popular(file_name):
    # use defaultdict to create a dictionary with 0 as value
    d = defaultdict(lambda: 0, {})
    with open(file_name) as file:
        for line in file:
            for word in line.split():
                d[word]+=1
    # return the top 10 most popular words
    top_10_count = sorted(d.values())[::-1][:10]
    top_10_counted_words = [key for key,value in d.items() if value in top_10_count][:10]
    print top_10_counted_words