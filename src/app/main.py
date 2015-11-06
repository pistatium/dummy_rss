# coding: utf-8

from datetime import datetime, timedelta

import pytz
from flask import Flask, make_response, render_template


app = Flask(__name__)

FEED_INTERVAL = 5
FEED_COUNT = 10


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/rss.xml")
def rss():
    now = datetime.now().timetuple()
    round_min = now[4] // FEED_INTERVAL * FEED_INTERVAL
    latest = datetime(*now[:4], round_min, tzinfo=pytz.utc)
    feed_times = [latest - timedelta(minutes=i * FEED_INTERVAL) for i in range(FEED_COUNT)]
    xml = render_template('rss.xml', feed_times=feed_times)
    response = make_response(xml)
    response.headers["Content-Type"] = "application/xml"
    return response


def main():
    app.run()

if __name__ == "__main__":
    main()
