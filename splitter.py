__author__ = 'zhaopeix'
import re


def split_sentence(file_name):
    result = ""
    with open(file_name) as _file:
        for line in _file:
            # use regex to substitute every matching pattern with a new line
            result += re.sub(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s',"\n", line)
    return result

