def molemass(sequence):
    #elements of H,C,N,O,P,S,K,F
    elements = ["H", "C", "N", "O", "P", "S", "K", "F"]
    #mass of respective elements
    mass = [1.0079, 12.0107, 14.0067, 15.9994, 30.9738, 32.0660, 39.0983, 18.9984]
    atoms = dict(zip(elements, mass))
    total_mass = 0
    for x in range(len(sequence)):
        total_mass += atoms[sequence[x]]
    return total_mass