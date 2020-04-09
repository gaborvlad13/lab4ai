def modularity(communities, param):
    noNodes = param['noNodes']
    mat = param['mat']
    toReturn = 0
    firsNode = communities[0]
    nextNode = communities[0]
    for i in range(0, noNodes):
       toReturn+=mat[nextNode][communities[i]]
       nextNode = communities[i]
    toReturn+=mat[communities[noNodes-1]][firsNode]
    return toReturn

def modularityTSP(communities, param):
    noNodes = param['noNodes']
    mat = param['mat']
    toReturn = 0
    firsNode = communities[0]
    nextNode = communities[0]
    for i in range(0, noNodes):
       toReturn+=mat.item((nextNode, communities[i]))
       nextNode = communities[i]
    toReturn+=mat.item((noNodes-1,firsNode))
    return toReturn
