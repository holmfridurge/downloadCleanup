import os
import re

t1 = '8 Out of 10 Cats S11E11 Best Bits WS PDTV .avi'
t2 = '''downloads/8 Out of 10 Cats - Season 7\\8 out of 10 cats S11 Uncut\\
    8 Out of 10 Cats S11E10 - Uncut.avi', 'downloads/8 Out of 10 Cats - Season 7\\
    8 out of 10 cats S11 Uncut\\8 Out of 10 Cats S11E11 Best Bits WS PDTV [SKID].avi'''

rending = '(\.avi$|\.mkv$\.rar$\.mp4$){1}'
repisode = '(E|e|Episode|episode)(\d{1,2})'
rseason = '(S|s|Season|season)(\d{1,2})'
regex = r'(.*)([ -_\.]){1}' + rseason + repisode +'(.)*' + rending


def compress(s):
        return re.sub('[(){}<>\-\.; ]', '', s).lower()
    
def ff(direct,s):

    regex = r'(.*)([ -_\.]){1}(S|s|Season|season)(\d{1,2})(E|e|Episode|episode)(\d{1,2})(.)*(\.avi$|\.mkv$){1}'
    
    name = compress(s)

    #files = [os.path.join(root,file) for root,_,files in os.walk(direct) for file in files
     #        if re.search(regex,file) != None and compress(re.search(regex,file).group(1).split('\\')[2]) == name]
    allshows = [os.path.join(root,file) for root,_,files in os.walk(direct) for file in files]
    searchedorshows = [show for show in allshows if re.search(regex,show.split('\\')[-1]) != None
                     and compress(re.search(regex,show).group(1).split('\\')[-1]) == name]
    return searchedorshows

    
