import subprocess
from datetime import datetime
import separationengine as se

print("It takes a while to do something, don't worry ;)")

process = subprocess.Popen("/usr/sbin/tcpdump", stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1)

for line in iter(process.stdout.readline, ''):
    se.strip(line.decode("UTF-8"));

process.communicate()
