import os
import re

t1 = '8 Out of 10 Cats S11E11 Best Bits WS PDTV .avi'
t2 = '''downloads/8 Out of 10 Cats - Season 7\\8 out of 10 cats S11 Uncut\\
    8 Out of 10 Cats S11E10 - Uncut.avi', 'downloads/8 Out of 10 Cats - Season 7\\
    8 out of 10 cats S11 Uncut\\8 Out of 10 Cats S11E11 Best Bits WS PDTV [SKID].avi'''
rending = '(\.avi$|\.mkv$\.rar$\.mp4$){1}'
repseason1 = '(S|s|Season|season)(\d{1,2})(E|e|Episode|episode)(\d{1,2})|(\[)(\d{1,2})([.xX-_])(\d{1,2})(\])'
repseason2 = '(\[)(\d{1,2})([.xX-_])(\d{1,2})(\])|(S|s|Season|season)(\d{1,2})(E|e|Episode|episode)(\d{1,2})'

regex = r'(.*)([ -_\.]){1}' + repseason1 + '(.)*' + rending


def compressname(s):
    return re.sub('[(){}<>\-\.; ]', '', s).lower()

def compressseason(s):
    if re.search(repseason1,s).group(1) != None:
        return "s" + re.search(repseason1,s).group(2) + "e" + re.search(repseason1,s).group(4)
    else:
        return "s" + re.search(repseason2,s).group(2) + "e" + re.search(repseason2,s).group(4)

# TO DO: Leyfa . bil _- a milli e og s
# TO DO: gripa villu tegar thattur sem leitar er af er ekki til
# TO D0: gripa villu thegar format ekki til i compressepseason og compressname
    
def ff(direct,s):

    #regex = r'(.*)([ -_\.]){1}(S|s|Season|season)(\d{1,2})(E|e|Episode|episode)(\d{1,2})(.)*(\.avi$|\.mkv$){1}'

    rending = '(\.avi$|\.mkv$\.rar$\.mp4$){1}'
    repseason = '((S|s|Season|season)(\d{1,2})(E|e|Episode|episode)(\d{1,2})|(\[\d{1,2}[.x]\d{1,2}\]))'
    regex = r'(.*)([ -_\.]){1}' + repseason + '(.)*' + rending
    
    name = compressname(s)

    allshows = [os.path.join(root,file) for root,_,files in os.walk(direct) for file in files]
    sshows = [show for show in allshows if re.search(regex,show.split('\\')[-1]) != None
                     and name in compressname(re.search(regex,show).group(1).split('\\')[-1])]

    newnames = [compressname(re.search(regex,show).group(1).split('\\')[-1]) for show in sshows]
    newseasons = [compressseason(re.search(regex,show).group(3).split('\\')[-1]) for show in sshows]
    newshows = [a + '.' +b for a,b in zip(newnames,newseasons)]
    
    return newshows

#TESTS
#print(len(ff("downloads","8.Out.Of.10.Cats"))) #56
#print(len(ff("downloads","30 Rock"))) #36
#print(len(ff("downloads","30 Ro"))) #36

    
