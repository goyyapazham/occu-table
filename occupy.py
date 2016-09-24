from flask import Flask, render_template
import random

# open file and sanitize data
## takes no inputs
def get_file():
    f = open("occupations.csv", "r")
    L = f.readlines()[1:-1]
    for i in range(len(L)):
        L[i] = L[i].replace('\"', '')
        x = L[i].rfind(",")
        L[i] = [ L[i][:x], float(L[i][x+1:-1]) ]
    return L

# create dictionary, key:val, where key=job class & val=pctage
## takes list returned from get_file() as input
def make_dict( L ):
    d = { }
    for i in range(len(L)):
        d[L[i][0]] = L[i][1]
    return d

# use pct values to set up a list of pct ranges, thru which we can specify
# a minimum and maximum in which a randomly selected value would denote a
# particular occupation
## takes list returned from get_file() as input
def set_ranges( L ):
    M = [ L[0][1] ]
    L = L[1:]
    for i in range(len(L)):
        M += [ round( (M[i]+L[i][1]), 1 ) ]
    return M

# iterates thru set_ranges() to ID occupation pinpointed by random number,
# then IDs associated occupation
## takes list from set_ranges() and dictionary from make_dict() as inputs
def randomizer( r, d ):
    rand = random.random() * 99.8
    x = 0
    while x < len(r):
        if rand <= r[x]:
            break
        x += 1
    for key in d:
        if x==0:
            return key
        x -= 1
    return "none"

## setting up the Flask app
app = Flask(__name__)

@app.route("/")
def run():
    lines = get_file()
    ranges = set_ranges(lines)
    duck = make_dict(lines)
    x = randomizer(ranges, duck)
    return render_template("main.html", title = "TITLE", r = random.randint(100,200), g = random.randint(100, 200), b = random.randint(100, 200), header = "So you want to get a job?", heading1 = "OCCUPATION", heading2 = "PERCENTAGE", d = duck.items(), rjob = x, jprob = duck[x])

if __name__ == '__main__':
    app.debug = True
    app.run()
