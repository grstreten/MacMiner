import subprocess
from datetime import datetime
import separationengine as se
import threading
from flask import Flask, request, render_template

def tcpdump_thread():
    print("It takes a while to do something, don't worry ;)")
    process = subprocess.Popen("/usr/sbin/tcpdump", stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1)

    print("Awaiting data")
    for line in iter(process.stdout.readline, ''):
        se.strip(line.decode("UTF-8"));

    process.communicate()

tcpdumpt = threading.Thread(target=tcpdump_thread)
tcpdumpt.start()

app = Flask(__name__)
