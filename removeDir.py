import os, re
import findShowsRename as fsr

def remove(direct):
    #regex to find the file extension
    rending = fsr.rending
    allFiles = fsr.getAllFiles(direct)
    #remove all files that aren't a video format or .srt file
    for f in allFiles:
        filename, file_extension = os.path.splitext(f)
        if re.search(rending, file_extension) == None:
            os.remove(f)
    #remove all empty directories
    for root, dirs, files in os.walk(direct):
        for d in dirs:
            path = root+'/'+d
            if os.listdir(path)==[]:
                os.rmdir(path)
