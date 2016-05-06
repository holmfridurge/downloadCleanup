import os
import re

#GEYMSLA
#rending = '((\.avi$|\.mkv$|\.rar$|\.mp4$){1})'
#rseason = '(((S|s|Season|season)(\d{1,2})(E|e|Episode|episode)(\d{1,2}))|((\[)(\d{1,2})([.xX-_])(\d{1,2})(\])))'
#rseason = '(((S|s|Season|season)(\d{1,2})(E|e|Episode|episode)(\d{1,2}))|((\[)(\d{1,2})([.xX-_])(\d{1,2})(\])))'

#Use two different regex so we can use catched groups
rseason1 = '(S|s|Season|season)(\d{1,2})(E|e|Episode|episode)(\d{1,2})|(\[)(\d{1,2})([.xX-_])(\d{1,2})(\])'
rseason2 = '(\[)(\d{1,2})([.xX-_])(\d{1,2})(\])|(S|s|Season|season)(\d{1,2})(E|e|Episode|episode)(\d{1,2})'


def compressname(s):
    return re.sub('[(){}<>\-\.; ]', '', s).lower()


def compressseason(s):
    if re.search(rseason1,s).group(4):
        return "s" + re.search(rseason1,s).group(2) + "e" + re.search(rseason1,s).group(4)
    else:
        return "s" + re.search(rseason2,s).group(2) + "e" + re.search(rseason2,s).group(4)

# TO DO: 
# TO DO: Leyfa . bil _- a milli e og s
# TO DO: numer a thattum

    
def ff(direct,s):

    #regex = r'(.*)([ -_\.]){1}(S|s|Season|season)(\d{1,2})(E|e|Episode|episode)(\d{1,2})(.)*(\.avi$|\.mkv$){1}'

    #rending = '((\.avi$|\.mkv$|\.rar$|\.mp4$){1})'
    #rseason = '((S|s|Season|season)(\d{1,2})(E|e|Episode|episode)(\d{1,2})|(\[\d{1,2}[.x]\d{1,2}\]))'
    #regex = r'(.*)([ -_\.]){1}' + rseason + '(.*)' + rending
    rseason = '(((S|s|Season|season)(\d{1,2})(E|e|Episode|episode)(\d{1,2}))|((\[)(\d{1,2})([.xX-_])(\d{1,2})(\])))'
    rending = '((\.avi|\.mkv|\.mp4|\.rar){1})'
    regex = '(.+)(([ -_\.]){0,1})' + rseason + '(.*)' + rending
    #regexlong = '(.+)(([ -_\.]){0,1})(((S|s|Season|season)(\d{1,2})(E|e|Episode|episode)(\d{1,2}))|((\[)(\d{1,2})([.xX-_])(\d{1,2})(\])))(.*)((\.avi|\.mkv|\.mp4|\.rar){1})'
    
    name = compressname(s)

    allshows = [os.path.join( root,file) for root,_,files in os.walk(direct) for file in files]
    sshows = [show for show in allshows if re.search(regex,show.split('\\')[-1]) != None
                     and name in compressname(re.search(regex,show).group(1).split('\\')[-1])]

    newnames = [compressname(re.search(regex,show).group(1).split('\\')[-1]) for show in sshows]
    newseasons = [compressseason(re.search(rseason,show).group(1).split('\\')[-1]) for show in sshows]
    endings = [re.search(rending,show).group(1).split('\\')[-1] for show in sshows]
    newshows = [name + "." + season + ending for name, season, ending in zip(newnames,newseasons,endings)]

    #newseasons = [compressseason(re.search(regex,show).group(2).split('\\')[-1]) for show in sshows]
    #newendings = [re.search(regex,show).group(4).split('\\')[-1] for show in sshows]
    #newshows = [a + '.' +b for a,b in zip(newnames,newseasons)]
    #parsedshows =[re.findall(regex, show, re.VERBOSE) for show in sshows]
    

    # Returns the name of the shows that was searched for
    return newshows

#TESTS
#print(len(ff("downloads","8.Out.Of.10.Cats")) #Result: 69
#print(len(ff("downloads","30 Rock"))) #Result: 61
#print(len(ff("downloads","30 Ro")))  #Result> 61
#ff('downloads','30 Ro')

    
