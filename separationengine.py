import re
from collections import deque

inQueue = deque(maxlen=10)
outQueue = deque(maxlen=10)

def strip(text):
    inmatch = re.search("IP\\s(\\S+)", text)
    if not inmatch:
        inmatch = re.search("IP6\\s(\\S+)", text)

    instring = ""
    if inmatch:
        instring = inmatch.group(1)

    outstring = ""
    outmatch = re.search(">\\s(\\S+)", text)
    if outmatch:
        outstring = outmatch.group(1)[0:-1]

    if inmatch or outmatch:
        if instring not in inQueue:
            inQueue.append(instring)
        if outstring not in outQueue:
            outQueue.append(outstring)

    print(inQueue[-1] + " " + outQueue[-1])
