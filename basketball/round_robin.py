def roundRobin(units, sets=None):
    """ Generates a schedule of "fair" pairings from a list of units """
    if len(units) % 2:
        units.append(None)
    count    = len(units)
    sets     = (count - 1)*2
    half     = int(count / 2)
    schedule = []
    flip = False
    for turn in range(sets):
        pairings = []
        for i in range(half):
            if not flip:
                pairings.append((units[i], units[count-i-1]))
            else:
                pairings.append((units[count-i-1], units[i]))
        units.insert(1, units.pop())
        schedule.append(pairings)
        if turn == count-1:
          flip = True
    return schedule