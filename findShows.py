import os, re, shutil
import findShowsRename as fsr

def tester(d):
    sshows = list(fsr.findshows(d))
    for i in sshows:
        print(i)

def moveShows(direct,s=''):
    rseason1 = fsr.rseason1
    sshows = list(fsr.findshows(direct))
    for i in sshows:
        season = getSeason(i[1])
        sname = getName(i[1])
        dirName = 'Shows/'+sname+'/'+season+'/'
        if not os.path.exists(dirName):
            os.makedirs(dirName)
        shutil.move(i[0], dirName+i[1])
    
def getSeason(s):
    rseason = '(s)(\d{1,2})(e)(\d{1,2})'
    b = fsr.compressseason(s)
    if re.search(rseason,b):
        b = re.search(rseason,b).group(2)
    return 'Season '+ b

def getName(s):
    c = s.split('.')
    return c[0]

def moveMovies(direct,s=''):
    smovies = list(fsr.findmovies(direct))
    for i in smovies:
        dirName = 'Movies/'
        if not os.path.exists(dirName):
            os.makedirs(dirName)
        shutil.move(i[0], dirName)
#TESTS
#print(len(findshows("downloads","8.Out.Of.10.Cats")) #Result: 69
#print(len(findshows("downloads","30 Rock"))) #Result: 61
#print(len(findsows("downloads","30 Ro")))  #Result> 61
#findshows('downloads','30 Ro')
