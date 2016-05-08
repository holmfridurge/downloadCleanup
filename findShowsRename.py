import os
import re

#global so we can use across files and functions
rseason1 = '(S|s|Season|season)([ \-\_\.]*)(\d{1,2})([ \-\_\.]*)(E|e|Episode|episode)([ \-\_\.]*)(\d{1,2})'
rseason2 = '(\[)*(\d{1,2})([\.xX\-\_ ])(\d{1,2})(\])*'
rseason3 = '(([\-\_\[#]+)(\d{1,3})(\]*))'
rseason = '(' + rseason1 + '|' + rseason2 +  '|' + rseason3 + ')'
rending = '((\.avi|\.mkv|\.mp4|\.rar|\.srt){1})'
regex = '(.+)(([ -_\.]){0,1})' + rseason + '(.*)' + rending
ryear = '(19|20)\d{2}'

def compressname(s):
    return re.sub('[\[\](){}<>\+\-\.\_; ]', '', s).lower()

def compressseason(s):
    if re.search(rseason1,s):
        return 's' + re.search(rseason1,s).group(3).lstrip('0') + 'e' + re.search(rseason1,s).group(7).lstrip('0')
    elif re.search(rseason2,s):
        return 's' + re.search(rseason2,s).group(2).strip('0') + 'e' + re.search(rseason2,s).group(4).lstrip('0')
    else:
        #can not evaluate season/eiposde number, use original string.
        return ''

def findshows(direct,s = ''):
    allfiles = [os.path.join(root,file) for root,_,files in os.walk(direct) for file in files]
    if s == '':
        #full path of all shows
        sshows = [show for show in allfiles if re.search(regex,show.split('\\')[-1]) != None]
    else:
        name = compressname(s)
        #full path of shows that have name which include the searched string
        sshows = [show for show in allfiles if re.search(regex,show.split('\\')[-1]) != None
                     and name in compressname(re.search(regex,show).group(1).split('\\')[-1])]

    #build new names for files
    newnames = [compressname(re.search(regex,show).group(1).split('\\')[-1]) for show in sshows]
    newseasons = [compressseason(re.search(rseason,show).group(1).split('\\')[-1]) for show in sshows]
    endings = [re.search(rending,show).group(1).split('\\')[-1] for show in sshows]
    newshows = [name + "." + season + ending for name, season, ending in zip(newnames,newseasons,endings)]
    
    return zip(sshows,newshows)

def findmovies(direct):
    allfiles = [os.path.join(root,file) for root,_,files in os.walk(direct) for file in files]
    movies = [show for show in allfiles if re.search(regex,show.split('\\')[-1]) == None
              and re.search(rending,show.split('\\')[-1])
              and re.search(ryear,show.split('\\')[-1])]
    return zip(movies)

def getAllFiles(direct):
    allFiles = [os.path.join(root,file) for root,_,files in os.walk(direct) for file in files]
    return allFiles
