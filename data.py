# -*- coding: utf-8 -*-

import urllib2, re, json
import oauth2
import csv
import recommendations
import time

def imdbAPIbyTitle(title):
    api = 'http://mymovieapi.com/'
    paras = {'title': title}
    r = oauth2.Request('GET', api, paras)
    url = r.to_url()
    rawfile = urllib2.urlopen(url)
    jsonFile = rawfile.read()
    movie = json.loads(jsonFile)
    return json.dumps(movie)

def processMovie(path='data'):
    with open(path + '/data.csv', 'wb') as f:
        csv_writer = csv.writer(f)

        for line in open(path + '/movielens/u.item'):
            id = line.split('|')[0]
            title = line.split('|')[1]
            movietime = line.split('|')[2]
            if movietime != '':
                movietime = time.strftime('%m/%d/%Y', time.strptime(movietime, '%d-%b-%Y'))
            movieurl = line.split('|')[4]
            ls = []
            
            m = re.match(r"(.*)(\(\d+\))", title)
            if m:
                movie = m.group(1).strip(' ')
                if '(' in movie and ')' in movie:
                    movie = movie.split('(')[1].rstrip(')')
                  
            try:
                moviejson = json.loads(imdbAPIbyTitle(unicode(movie)))
                if isinstance(moviejson, list):
                    moviecover = moviejson[0].get('poster', {}).get('imdb', 'static/images/nocover.png')
                    if moviecover == None:
                        moviecover = 'static/images/nocover.png'
            except:
                moviecover = 'static/images/nocover.png'
            
            ls.append(title)
            ls.append(movie)
            ls.append(movietime)
            ls.append(unicode(moviecover).encode('utf-8'))
            ls.append(movieurl)
            csv_writer.writerow(ls)
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
# processMovie()

# Build similarity matrix
# prefs = recommendations.loadMovieLens()
# sim = buildSimMatrix(prefs)
# print sim

# Load
# loadSimMatrix()