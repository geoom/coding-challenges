# uva100 Station Balance
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=351


def masses_collection(input, chambers_quantity, specimens_quantity):
    
    spec_masses_from_input = input[2: 2 + specimens_quantity]
    dummy_spec_masses = [ 0 for _ in range(2*chambers_quantity - specimens_quantity)]

    spec_masses_collection = spec_masses_from_input + dummy_spec_masses
    spec_masses_collection.sort()

    return spec_masses_collection


def chambers_assisgments(spec_masses, chambers_quantity):
    
    assisgments = []
    
    for idx in range(chambers_quantity):
            
        assigment_on_chamber = [
            spec_masses[idx],
            spec_masses[-(idx + 1)]
        ]

        assisgments.append(assigment_on_chamber)

    return assisgments


def average_chamber_mass(spec_masses_collection, chambers_quantity):
    return float(sum(spec_masses_collection))/float(chambers_quantity)


def imbalance(assisgments, spec_masses_collection, chambers_quantity):
    imbalance = 0

    for idx in range(len(assisgments)):
        imbalance = imbalance + abs(total_chamber_mass(assisgments[idx]) - average_chamber_mass(spec_masses_collection, chambers_quantity))

    return imbalance


def total_chamber_mass(specimens_masses):
    return sum(specimens_masses)


def process_set_input(array_inputs):

    for idx, input in enumerate(array_inputs):
        
        print "Set #%d" % (idx + 1)

        chambers_quantity = input[0]
        specimens_quantity = input[1]

        spec_masses_collection = masses_collection(
            input, chambers_quantity, specimens_quantity
        )

        assisgments_collection = chambers_assisgments(
            spec_masses_collection, chambers_quantity
        )

        for idx in range(len(assisgments_collection)):
            print "%d: %s" % (
                    idx, 
                    ' '.join([ str(el) for el in filter(lambda mass: mass != 0, assisgments_collection[idx])])
                )

        print "IMBALANCE = %s \n" % '{:.5f}'.format(imbalance(assisgments_collection, spec_masses_collection, chambers_quantity))
        
# Exec
data_input = [
    [ 2, 3, 6, 3, 8 ],
    [ 3, 5, 51, 19, 27, 14, 33],
    [5, 9, 1, 2, 3, 5, 7, 11, 13, 17, 19]
]

process_set_input(data_input)