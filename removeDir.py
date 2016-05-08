import os, re
import findShowsRename as fsr

def remove(direct):
    rending = fsr.rending
    allFiles = fsr.getAllFiles(direct)
    for f in allFiles:
        filename, file_extension = os.path.splitext(f)
        if re.search(rending, file_extension) == None:
            os.remove(f)
    for root, dirs, files in os.walk(direct):
        for d in dirs:
            path = root+'/'+d
            if os.listdir(path)==[]:
                os.rmdir(path)
