import findShows as fs
import removeDir as rd
def organize(direct, s = ''):
    fs.moveShows(direct, s)
    fs.moveMovies(direct, s)
    rd.remove(direct)
