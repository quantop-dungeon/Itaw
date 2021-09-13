def generate_trace(dx=0):
    """Generates parabolas offset along x by dx."""
    xarr = range(-10, 10)
    yarr = [(x+dx)**2 for x in xarr]
    return {'x': xarr, 'y': yarr} 

from itatools import itaw

win = itaw(generate_trace)