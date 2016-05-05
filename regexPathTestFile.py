import os
import re

t1 = '8 Out of 10 Cats S11E11 Best Bits WS PDTV .avi'
t2 = '''downloads/8 Out of 10 Cats - Season 7\\8 out of 10 cats S11 Uncut\\
    8 Out of 10 Cats S11E10 - Uncut.avi', 'downloads/8 Out of 10 Cats - Season 7\\
    8 out of 10 cats S11 Uncut\\8 Out of 10 Cats S11E11 Best Bits WS PDTV [SKID].avi'''
rending = '(\.avi$|\.mkv$\.rar$\.mp4$){1}'
repseason = '((S|s|Season|season)(\d{1,2})(E|e|Episode|episode)(\d{1,2})|(\[\d{1,2}[.x]\d{1,2}\]))'
regex = r'(.*)([ -_\.]){1}' + repseason + '(.)*' + rending



def compress(s):
        return re.sub('[(){}<>\-\.; ]', '', s).lower()

# TO DO: gripa villu tegar thattur sem leitar er af er ekki til
# Geta slad inn partial nofn
    
def ff(direct,s):

    #regex = r'(.*)([ -_\.]){1}(S|s|Season|season)(\d{1,2})(E|e|Episode|episode)(\d{1,2})(.)*(\.avi$|\.mkv$){1}'

    rending = '(\.avi$|\.mkv$\.rar$\.mp4$){1}'
    repseason = '((S|s|Season|season)(\d{1,2})(E|e|Episode|episode)(\d{1,2})|(\[\d{1,2}[.x]\d{1,2}\]))'
    regex = r'(.*)([ -_\.]){1}' + repseason + '(.)*' + rending
    
    name = compress(s)

    allshows = [os.path.join(root,file) for root,_,files in os.walk(direct) for file in files]
    sorshows = [show for show in allshows if re.search(regex,show.split('\\')[-1]) != None
                     and name in compress(re.search(regex,show).group(1).split('\\')[-1])]
    return sorshows

#TESTS
print(len(ff("downloads","8.Out.Of.10.Cats"))) #56
print(len(ff("downloads","30 Rock"))) #36
print(len(ff("downloads","30 Ro"))) #36

    
