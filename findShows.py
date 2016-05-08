import os, re, shutil
import findShowsRename as fsr

#move all tv shows to a folder named Shows and subdirectories after the season number
def moveShows(direct,s=''):
    sshows = list(fsr.findshows(direct))
    for i in sshows:
        season = getSeason(i[1])
        sname = getName(i[1])
        dirName = 'Shows/'+sname+'/'+season+'/'
        #check if directory exists, if not a new one is created
        if not os.path.exists(dirName):
            os.makedirs(dirName)
        #move the file and rename it
        shutil.move(i[0], dirName+i[1])

#get season number
def getSeason(s):
    rseason = '(s)(\d{1,2})(e)(\d{1,2})'
    #get compressed name so it's easier to get the season number
    b = fsr.compressseason(s)
    if re.search(rseason,b):
        b = re.search(rseason,b).group(2)
    return 'Season '+ b

#get name of tv show
def getName(s):
    c = s.split('.')
    return c[0]

#move all movies to a directory named Movies
def moveMovies(direct,s=''):
    smovies = list(fsr.findmovies(direct))
    for i in smovies:
        dirName = 'Movies/'
        #check if directory exists, if not a new one is created
        if not os.path.exists(dirName):
            os.makedirs(dirName)
        #move the file to Movies directory
        shutil.move(i[0], dirName)
#TESTS
#print(len(findshows("downloads","8.Out.Of.10.Cats")) #Result: 69
#print(len(findshows("downloads","30 Rock"))) #Result: 61
#print(len(findsows("downloads","30 Ro")))  #Result> 61
#findshows('downloads','30 Ro')
