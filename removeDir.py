import os, re
import findShowsRename as fsr

rending = '((\.avi|\.mkv|\.mp4|\.rar){1})'

def remove():
    allFiles = fsr.getAllFiles('testSub')
    for f in allFiles:
        filename, file_extension = os.path.splitext(f)
        if re.search(rending, file_extension) == None:
            print(f)
            os.remove(f)
    for root, dirs, files in os.walk('testSub'):
        for d in dirs:
            path = root+'/'+d
            if os.listdir(path)==[]:
                print(path)
                os.rmdir(path)
