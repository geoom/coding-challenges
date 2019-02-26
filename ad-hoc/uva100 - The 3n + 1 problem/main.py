import sys

def cycle_length(n):

    def cycle(n, param_count):

        count = param_count + 1
        # print n,

        if n != 1:
            if n % 2 != 0:
                n = 3 * n + 1
            else:
                n = n / 2

            return cycle(n, count)
        else:
            return count

    return cycle(n, 0)


def max_cycle_length(first, second):
    
    max_value = -1

    if first > second:
        first, second = second, first

    while(first <= second):
        current_cycle_length = cycle_length(first)

        if current_cycle_length > max_value:
            max_value = current_cycle_length

        first = first + 1

    return max_value


if __name__ == '__main__':

    for line in sys.stdin:
        start, end = map(int, line.split()[:2])
        print(start, end, max_cycle_length(start, end))

    exit(0)
