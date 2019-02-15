
# uva100 The 3n+1 problem
# https://uva.onlinejudge.org/index.php?Itemid=8&option=com_onlinejudge&page=show_problem&problem=36

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

    iterator_number = first

    while(first <= second):
        current_cycle_length = cycle_length(first)

        if current_cycle_length > max_value:
            max_value = current_cycle_length

        first = first + 1

    return "%d, %d, %d" %  (iterator_number, second, max_value)

print max_cycle_length(1, 10)
print max_cycle_length(100, 200)
print max_cycle_length(201, 210)
print max_cycle_length(900, 1000)
