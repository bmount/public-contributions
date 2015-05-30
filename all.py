import datetime
import os

DAY = 24*60*60
WEEK = 7*DAY

start_heart = datetime.datetime.strptime("2015-05-26 12:34:56", "%Y-%m-%d %H:%M:%S")

def fmt(d, t=start_heart):
    s = t + datetime.timedelta(seconds=d)
    return datetime.datetime.strftime(s, "%s -0700")

def commit(tstr):
    os.environ['GIT_AUTHOR_DATE'] = tstr
    #os.environ['GIT_COMMITTER_DATE'] = tstr
    os.system("echo %s >> tmpfile" % tstr)
    os.system("git commit -am \"%s\"" % tstr)

intervals = [
        [    WEEK,  -DAY],
        [2 * WEEK,  -DAY],
        [3 * WEEK,  0],
        [3 * WEEK,  DAY],
        [2 * WEEK,  2 * DAY],
        [1 * WEEK,  3 * DAY ]]


if __name__ == '__main__':
    os.system("git init && touch tmpfile && git add tmpfile")
    dates = []
    for i in intervals:
        for j in [-1,1]:
            dates.append(fmt(j*i[0] + i[1]))

    history = sorted(dates, reverse=True)
    for t in history:
        commit(t)
        commit(t)

    commit(fmt(0))
    commit(fmt(0))
    tip = 4 * DAY
    commit(fmt(tip))
    os.system("git add .")
    commit(fmt(tip))
