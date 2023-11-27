import math
import random
def argmaxallval(gen):
    """
    gen list que genere pares(elem, value)
    reenvoie list des elements avec valeurs maximal
    """
    vmax=-math.inf
    maxvls=[]
    for (e,v) in gen:
        if v>vmax:
            maxvls, vmax= [e],v
        elif v==vmax:
            maxvls.append(e)
    return maxvls

def argmaxelement(gen):
    """
    reenvoie un element avec le maximal valeur dans une list de valeurs.
    Si il a plusier valeur maximal, le valeur maximal se return random(al hazard)
    """
    return random.choice(argmaxallval(gen))

def argmalist(list):
    """
    return el indice de la valeur plus grand
    """
    return argmaxelement(enumerate(list))
print(argmalist([2,33,4,55,3,2]))
def argmaxdict(dct):
    """
    reenvoie el indice plus gand dans une dictionaire
    """
    return argmaxelement(dct.items())
print(argmaxdict({3:5, 7:55,8:3}))
