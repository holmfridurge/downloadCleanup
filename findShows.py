import os, re, shutil
import findShowsRename as fsr

def moveFiles(direct,s):
    rseason1 = fsr.rseason1
    sshows = fsr.findshows(direct,s)
    for i in sshows:
        season = getSeason(i[1])
        sname = getName(i[1])
        dirName = 'Shows/'+sname+'/'+season+'/'
        if not os.path.exists(dirName):
            os.makedirs(dirName)
        shutil.move(i[0], dirName+i[1])
        print(dirName)

def getSeason(s):
    rseason = fsr.rseason1
    b = fsr.compressseason(s)
    b = re.search(rseason,b).group(2)
    b = b.lstrip('0')
    return 'Season '+b

def getName(s):
    c = s.split('.')
    return c[0]


#TESTS
#print(len(findshows("downloads","8.Out.Of.10.Cats")) #Result: 69
#print(len(findshows("downloads","30 Rock"))) #Result: 61
#print(len(findsows("downloads","30 Ro")))  #Result> 61
#findshows('downloads','30 Ro')
