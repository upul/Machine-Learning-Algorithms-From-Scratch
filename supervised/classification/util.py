def print_result(iteration, cost):
    if (iteration <= 10) or \
        (iteration <= 100 and iteration % 10 == 0) or \
        (iteration <= 1000 and iteration % 100 == 0) or \
        (iteration <= 10000 and iteration % 1000 == 0) or \
        (iteration <= 100000 and iteration % 10000 == 0) or \
            (iteration > 100000 and iteration % 50000 == 0):
        print('iteration: {:10d}\t\tcost: {:1.4e}'.format(iteration, cost))