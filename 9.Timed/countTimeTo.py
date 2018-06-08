import time

def timed(function): #O(const)
    start_time = time.time()
    solution = function
    time_lapse = time.time() - start_time
    res = str(solution) + ' in ' + str(time_lapse*1000) + ' milliseconds'
    print res
