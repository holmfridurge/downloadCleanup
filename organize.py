import moveFiles as mf
import removeDir as rd
def organize(direct, s = ''):
    mf.moveShows(direct, s)
    mf.moveMovies(direct, s)
    rd.remove(direct)
