def witch_hunt(suspect_sets: set, innocent_sets: set) -> set:
    witches = set()

    for sets in suspect_sets:
        if witches:
            witches = witches & sets
        else:
            witches = sets.copy()
    for sets in innocent_sets:
        witches = witches - sets
    return witches
