import os
import re

#Use two different regex so we can use catched groups when compressins seasons
rseason1 = '(S|s|Season|season)(\d{1,2})(E|e|Episode|episode)(\d{1,2})|(\[)(\d{1,2})([.xX-_])(\d{1,2})(\])'
rseason2 = '(\[)(\d{1,2})([.xX-_])(\d{1,2})(\])|(S|s|Season|season)(\d{1,2})(E|e|Episode|episode)(\d{1,2})'


def compressname(s):
    return re.sub('[(){}<>\-\.; ]', '', s).lower()

def compressseason(s):
    if re.search(rseason1,s).group(4):
        return "s" + re.search(rseason1,s).group(2) + "e" + re.search(rseason1,s).group(4)
    else:
        return "s" + re.search(rseason2,s).group(2) + "e" + re.search(rseason2,s).group(4)

def findshows(direct,s):

    rseason = '(((S|s|Season|season)(\d{1,2})(E|e|Episode|episode)(\d{1,2}))|((\[)(\d{1,2})([.xX-_])(\d{1,2})(\])))'
    rending = '((\.avi|\.mkv|\.mp4|\.rar){1})'
    regex = '(.+)(([ -_\.]){0,1})' + rseason + '(.*)' + rending
    #regexlong = '(.+)(([ -_\.]){0,1})(((S|s|Season|season)(\d{1,2})(E|e|Episode|episode)(\d{1,2}))|((\[)(\d{1,2})([.xX-_])(\d{1,2})(\])))(.*)((\.avi|\.mkv|\.mp4|\.rar){1})'

    
    name = compressname(s)

    allshows = [os.path.join(root,file) for root,_,files in os.walk(direct) for file in files]
    sshows = [show for show in allshows if re.search(regex,show.split('\\')[-1]) != None
                     and name in compressname(re.search(regex,show).group(1).split('\\')[-1])]

    newnames = [compressname(re.search(regex,show).group(1).split('\\')[-1]) for show in sshows]
    newseasons = [compressseason(re.search(rseason,show).group(1).split('\\')[-1]) for show in sshows]
    endings = [re.search(rending,show).group(1).split('\\')[-1] for show in sshows]
    newshows = [name + "." + season + ending for name, season, ending in zip(newnames,newseasons,endings)]

    returnShows = list(zip(sshows,newshows))
    return returnShows
    # Returns a list containg the names of the shows that was searched for and compressed filenames
   # return [sshows,newshows]

def getAllFiles(direct):
    allshows = [os.path.join(root,file) for root,_,files in os.walk(direct) for file in files]
    return allshows

