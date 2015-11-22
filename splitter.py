__author__ = 'zhaopeix'
import re


def split_sentence(file_name):
    result = ""
    with open(file_name) as _file:
        for line in _file:
            result += re.sub(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s',"\n", line)
    return result

