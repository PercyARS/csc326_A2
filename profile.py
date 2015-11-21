__author__ = 'zhaopeix'

from time import clock

PROFILE_FUNCTIONS = True
# This dictionary will store the number of runs each function has had
PROFILE_RUNS = {}
PROFILE_RESULTS = {}

def profile(func):
    def new(*args, **kwargs):
        # if the runtime is  required
        if PROFILE_FUNCTIONS:
            start = clock()
            ret = func(*args, **kwargs)
            duration = clock() - start
            # if this function hasn't been run before
            if func.__name__ not in PROFILE_RUNS:
                PROFILE_RUNS[func.__name__] = 1
                PROFILE_RESULTS[func.__name__] = duration
            else:
                # increment the number of runs
                num_of_runs = PROFILE_RUNS[func.__name__]
                PROFILE_RUNS[func.__name__] += 1
                # the result is (old_result * previous number of runs + duration)/(previous number of runs+1)
                new_result = (PROFILE_RESULTS[func.__name__] * num_of_runs + duration)/PROFILE_RUNS[func.__name__]
        else:
            # if runtime is not required, simply return the function
            ret = func(*args, **kwargs)
        return ret
    return new



