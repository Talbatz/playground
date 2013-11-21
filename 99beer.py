
def beerz(numbah=100):
    assert numbah is not None, "Error !!!!"   
    list = []
    for i in range(numbah, -1, -1):
        list.append("%d bottles of beer on the wall" %i)
    return list;
    
        

for b in beerz():
    print b
