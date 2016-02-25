import pykov as pk

def substr(s, f, window):
    """Out-of-range-safe implementation of substring"""
    l = len(s)
    j = (f + window) % l
    if j == 0: j = l
    return s[f % l: j]

def train(data, window=2):
    model = pk.Chain()

    for rhythm in data:
        for i in range(0, len(rhythm), window):
            a = substr(rhythm, i, window)
            b = substr(rhythm, i + window, window)
            model[(a, b)] = model[(a, b)] + 1 if model.has_key((a, b)) else 1

    model.stochastic()
    return model

def generate(model, l, window=2):
    return ''.join(model.walk((l / window) - 1))
