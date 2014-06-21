import subprocess
from datetime import datetime
import threading
from flask import Flask, request, render_template

def tcpdump_thread():
    import separationengine as se
    print("It takes a while to do something, don't worry ;)")
    process = subprocess.Popen("/usr/sbin/tcpdump", stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1)

    print("Awaiting data")
    for line in iter(process.stdout.readline, ''):
        se.strip(line.decode("UTF-8"));

    process.communicate()

tcpdumpt = threading.Thread(target=tcpdump_thread)
tcpdumpt.start()

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html", usage={"hours" : 9, "charger" : 21}, app={"mostUsed", "Goat Simulator"}, network={"analytics" : 476})

@app.route("/data")
def data():
    return render_template("fulldata.html")

app.debug = True
app.run(host="0.0.0.0", port=6789)
