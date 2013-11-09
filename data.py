import urllib2, re, json
import oauth2
import csv
import recommendations

def imdbAPIbyTitle(title):
    api = 'http://mymovieapi.com/'
    paras = {'title': title}
    r = oauth2.Request('GET', api, paras)
    url = r.to_url()
    rawfile = urllib2.urlopen(url)
    jsonFile = rawfile.read()
    movie = json.loads(jsonFile)
    return json.dumps(movie)

def processMovie(prefs):
    with open('data/data.csv', 'wb') as f:
        c = csv.writer(f)
        dictLs = []
        keys = ['movie', 'time', 'cover', 'url']
        # for p in prefs:
        for i in prefs['1']:
            ls = []
            if i != 'unknown':
                m = re.match(r"(.*)(\(\d+\))", i)
                r_movie = i
                movie = m.group(1).strip(' ').split(',')[0]
                time = m.group(2).lstrip('(').rstrip(')')
                moviejson = json.loads(imdbAPIbyTitle(movie))
                if isinstance(moviejson, list):
                    cover = moviejson[0].get('poster', {}).get('imdb', 'static/images/nocover.png')
                    if cover == None:
                        cover = 'static/images/nocover.png'
                    url = moviejson[0].get('imdb_url', '')
                    ls.append(r_movie)
                    ls.append(movie)
                    ls.append(time)
                    ls.append(cover)
                    ls.append(url)
                    c.writerow(ls)                
                    print ls

def buildSimMatrix(prefs):
    sim = recommendations.calculateSimilarItems(prefs, n=10)
    return sim
    # with open('data/sim.csv', 'wb') as f:
    #     c = csv.writer(f)
    #     for key, value in sim.items():
    #         c.writerow([key, value])
            
# def loadSimMatrix():
#     r = csv.reader(open('data/sim.csv', 'rb'))
#     mydict = dict(x for x in r)
#     return mydict
    
# Build movie data
# prefs = recommendations.loadMovieLens()
# processMovie(prefs)

# Build similarity matrix
# prefs = recommendations.loadMovieLens()
# sim = buildSimMatrix(prefs)
# print sim

# Load
# loadSimMatrix()