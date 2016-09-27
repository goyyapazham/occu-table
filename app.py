from flask import Flask, render_template
from utils import occupy
import random

## setting up the Flask app
app = Flask(__name__)

@app.route("/")
def run():
    lines = occupy.get_file()
    ranges = occupy.set_ranges(lines)
    duck = occupy.make_dict(lines)
    x = occupy.randomizer(ranges, duck)
    return render_template("main.html", title = "TITLE", r = random.randint(100,200), g = random.randint(100, 200), b = random.randint(100, 200), header = "So you want to get a job?", heading1 = "OCCUPATION", heading2 = "PERCENTAGE", d = duck.items(), rjob = x, jprob = duck[x])

if __name__ == '__main__':
    app.debug = True
    app.run()
