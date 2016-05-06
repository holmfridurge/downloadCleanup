import os
import re
import shutil

def compressname(s):
    return re.sub('[(){}<>\-\.; ]', '', s).lower()

def findshows(direct,s):

    rseason = '(((S|s|Season|season)(\d{1,2})(E|e|Episode|episode)(\d{1,2}))|((\[)(\d{1,2})([.xX-_])(\d{1,2})(\])))'
    rending = '((\.avi|\.mkv|\.mp4|\.rar){1})'
    regex = '(.+)(([ -_\.]){0,1})' + rseason + '(.*)' + rending
    #regexlong = '(.+)(([ -_\.]){0,1})(((S|s|Season|season)(\d{1,2})(E|e|Episode|episode)(\d{1,2}))|((\[)(\d{1,2})([.xX-_])(\d{1,2})(\])))(.*)((\.avi|\.mkv|\.mp4|\.rar){1})'

    
    name = compressname(s)

    allshows = [os.path.join(root,file) for root,_,files in os.walk(direct) for file in files]
    sshows = [show for show in allshows if re.search(regex,show.split('\\')[-1]) != None
                     and name in compressname(re.search(regex,show).group(1).split('\\')[-1])]
    if not os.path.exists('Shows'):
        os.makedirs('Shows')

    for i in sshows:
        shutil.move(i, 'Shows/'+i.split('\\')[-1])
        print(i)
    # Returns a list containg the names of the shows that was searched for
    #return sshows

#TESTS
#print(len(findshows("downloads","8.Out.Of.10.Cats")) #Result: 69
#print(len(findshows("downloads","30 Rock"))) #Result: 61
#print(len(findsows("downloads","30 Ro")))  #Result> 61
#findshows('downloads','30 Ro')
