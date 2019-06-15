
# Time limit: 3.000 seconds

def get_out_of_well(H, V, D, F):
    distance_lost = F / 100.0 * V 
    climbed_height = 0
    succeded = False
    day = 0

    while not succeded and climbed_height >= 0 :
        day += 1
        climbed_height += V - (distance_lost * (day - 1))

        if climbed_height > H:
            succeded = True
        else:
            climbed_height -= D

    if succeded:
        print("success on day %s" % day)
    else:
        print("failure on day %s" % day)
    

if __name__ == "__main__":

    collection_input = [
        [6, 3, 1, 10],
        [10, 2, 1, 50],
        [50, 5, 3, 14],
        [50, 6, 4, 1],
        [50, 6, 3, 1],
        [1, 1 ,1 ,1],
        [0 ,0 ,0 ,0]
    ]

    for data_input in collection_input:
        if data_input[0] is not 0:
            get_out_of_well(*data_input)

    exit(0)