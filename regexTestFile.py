import os
import re
def compressstring(s):
        return re.sub('[(){}<>\-\.; ]', '', s)
def reg(s):

    g1 = re.search(r'(.*)([ \.]){1}(S|s|Season|season)(\d{1,2})(E|e|Episode|episode)(\d{1,2})[ .a-zA-Z]*',s)
    name = g1.group(1)
    compressedname = compressstring(name)


    testshows = ["bb.s01e01.avi","bb.S01E02.avi","bb s01e03.avi","bb S01E04.avi"]
    testshows += ["b.b.s01e05.avi", "b-b.s01e06.avi"]

    # listi med ollum nofnum

    # herna erum vid ad flokka shows i lista sem haegt er ad vinna med
    allshows =[re.findall(r"""(.*)          # Title
                        [ .]
                        (S|s|Season|season)(\d{1,2})    # Season
                        (E|e|Episode|episode)(\d{1,2})    # Episode
                        ([ .a-zA-Z]*)+  # Space, period, or words like PROPER/Buried
                        (\d{3,4}p)?   # Quality
                    """, test, re.VERBOSE) for test in testshows]
    
    # herna sigtum vid ut tha thaetti sem notandinn slo inn
    searchedshows = [x for x in allshows if compressstring(x[0][0]) == compressedname]

    # lista af full orginal nofnum
    # lista breyttum nofnum
    return searchedshows

