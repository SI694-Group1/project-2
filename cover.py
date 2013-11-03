import urllib2, re, json
import oauth2
import csv

def imdbAPIbyTitle(title):
    api = 'http://mymovieapi.com/'
    paras = {'title': title}
    r = oauth2.Request('GET', api, paras)
    url = r.to_url()
    rawfile = urllib2.urlopen(url)
    jsonFile = rawfile.read()
    movie = json.loads(jsonFile)
    return json.dumps(movie)

def loadMovieLens(path='data/movielens'):
    # Get movie titles
    movies = {}
    for line in open(path + '/u.item'):
        (id, title) = line.split('|')[0:2]
        movies[id] = title

    # Load data
    prefs = {}
    for line in open(path + '/u.data'):
        (user, movieid, rating, ts) = line.split('\t')
        prefs.setdefault(user, {})
        prefs[user][movies[movieid]] = float(rating)
    return prefs

def processMovie(prefs):
    c = csv.writer(open("data.csv", "wb")) 
    dictLs = []
    keys = ['movie', 'time', 'cover', 'url']
    for i in prefs['1']:
        ls = []
        if i != 'unknown':
            m = re.match(r"(.*)(\(\d+\))", i)
            movie = m.group(1).strip(' ').split(',')[0]
            time = m.group(2).lstrip('(').rstrip(')')
            moviejson = json.loads(imdbAPIbyTitle(movie))
            if isinstance(moviejson, list):
                cover = moviejson[0].get('poster', {}).get('cover', '')
                url = moviejson[0].get('imdb_url', '')
                ls.append(movie)
                ls.append(time)
                ls.append(cover)
                ls.append(url)
                c.writerow(ls)                
                print ls

prefs = loadMovieLens()
processMovie(prefs)