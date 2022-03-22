from string import ascii_letters, digits
from random import choice

allChars = ascii_letters + digits


def Idmaker(limit):
    id = '' 

    for i in range(limit): 
        id += choice(allChars)
    
    return id


def getId(modelInstance, limit):
    id = Idmaker(limit)

    modelClass = modelInstance.__class__

    if modelClass.objects.filter(shorturl = id).exists():
        getId(modelInstance)
    
    return id