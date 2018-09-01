
def loadmovienames():
    movienames={}
    with open("/Users/ppligade/downloads/ml-100k/u.item", encoding='latin-1') as f:
        for line in f:
            fields=line.split("|")
            movid=fields[0]
            movname=fields[1]
            movienames[int(movid)]=movname
        return movienames


def loadmovienames2():
    movienames={}
    with open("/Users/ppligade/downloads/ml-100k/u.item") as f:
        for line in f:
            fields=line.split("|")
            movid=fields[0]
            movname=fields[1]
            movienames[int(movid)]=movname
        return movienames

print(loadmovienames())