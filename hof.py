__author__ = 'zhaopeix'


def map(function, sequence, *sequence_1): # real signature unknown; restored from __doc__
    """
    map(function, sequence[, sequence, ...]) -> list

    Return a list of the results of applying the function to the items of
    the argument sequence(s).  If more than one sequence is given, the
    function is called with an argument list consisting of the corresponding
    item of each sequence, substituting None for missing values when not all
    sequences have the same length.  If the function is None, return a list of
    the items of the sequence (or a list of tuples if more than one sequence).
    """
    return [function(*i) for i in zip(sequence,*sequence_1)]


def filter(function_or_none, sequence): # known special case of filter
    """
    filter(function or None, sequence) -> list, tuple, or string

    Return those items of sequence for which function(item) is true.  If
    function is None, return the items that are true.  If sequence is a tuple
    or string, return the same type, else return a list.
    """

    if function_or_none == None:
        result = [i for i in sequence if i]
    else:
        result = [i for i in sequence if function_or_none(i)]
    ret = result
    if isinstance(sequence,tuple):
        ret = tuple(result)
    elif isinstance(sequence,str):
        ret = ''.join(result)
    return ret


def reduce(function, sequence, initial=None): # real signature unknown; restored from __doc__
    """
    reduce(function, sequence[, initial]) -> value

    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as a default when the
    sequence is empty.
    """
    result = initial
    # if sequence is not empty
    if sequence:
        # if the initial is not given
        if initial == None:
            result = sequence[0]
            sequence = sequence[1:]
        for x in sequence:
            result = function(result, x)
    return result
