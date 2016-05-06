import os
import re
def parse(direct,s):

    #test = "bbs01e02.txt"
    regex = s + "s[0-9]+e[0-9]+(.*)"
    #print(re.match(regex,test))

    # Walk through every folder and grab files that match regex
    files = [os.path.join(root,file) for root,_,files in os.walk(direct) for file in files
             if re.match(regex,file)]
    return files

    parse("submissions","bb")

    #readerobjs = [open(f, encoding="utf-8") for f in files]
    #dicts = []
    # make a list of directories
    #for obj in readerobjs:
     #   d = {}
      #  for line in obj :
       #    i = line.split()
        #   d[i[1]] = i[2]
        #dicts.append(d)
        
    #sorteddicts = sorted(dicts, key=lambda k: k['Date'])
    #results = [(d.get("Team"), d.get("Problem")) for d in sorteddicts]# if d.get("Classify") == "Accepted"] 
    #return results
