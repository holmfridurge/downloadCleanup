import os
import re
import shutil
def parse(direct,s):

    #test = "bbs01e02.txt"
    regex = s + "s[0-9]+e[0-9]+(.*)"
    #print(re.match(regex,test))
    # Walk through every folder and grab files that match regex
    files = [os.path.join(root,file) for root,_,files in os.walk(direct) for file in files
             if re.match(regex,file)]
    n = files[0].split('\\')
    if not os.path.exists('Submissions/Shows'):
        os.makedirs('Submissions/Shows')
    print(n[len(n)-1])
    shutil.move(files[0], 'Submissions/Shows/'+n[len(n)-1])
    #print(files[0][len(files)-1])
    return files

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

    #testcase
    #parse('submissions','bb')
