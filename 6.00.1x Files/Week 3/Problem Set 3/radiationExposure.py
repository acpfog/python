
def f(x):
    import math
    return 200*math.e**(math.log(0.5)/14.1 * x)

def radiationExposure(start, stop, step):
    if start + step >= stop:
        return step * f(start)
    else:
        return step * f(start) + radiationExposure(start + step, stop, step)

print radiationExposure(0, 3, 0.1)
