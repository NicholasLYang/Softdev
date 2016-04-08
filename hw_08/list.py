
def union (a, b):
    return  b + [x for x in a  if x not in b]

 
def intersection(a, b):
    return [x for x in b if x in a]

def set_diff(a, b):
    return [x for x in a if x not in b]

def sym_diff(a, b): 
    return [x for x in a if x not in b] + [x for x in b if x not in a]

def cart_product(a, b): # fairly sure this is an abelian group with sets
    return [(x, y) for x in a for y in b]
