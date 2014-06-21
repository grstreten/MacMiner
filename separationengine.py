import re
from collections import deque
import datadumper as dd

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
        duplicate = False
        if instring not in inQueue:
            inQueue.append(instring)
        else: duplicate=True
        if outstring not in outQueue:
            outQueue.append(outstring)
        else: duplicate=True

        if not duplicate:
            dd.insert_connection(inQueue[-1], outQueue[-1])
