#!/usr/bin/env python3

from bottle import post, run
import platform, subprocess, os

def cmd(cmd, stdout=subprocess.DEVNULL):
    return subprocess.Popen(cmd, shell=True, env=env, cwd=cwd, stdout=stdout)

url = "http://beta.hacksoc.org/servers/"
hostname = platform.node().split(".")[0]
# outfile = "{}.html".format(hostname) # TODO override this with argv
outfile = "index.html"

@post('/update')
def update():
    cmd('wget "{0}{1}.html" -O {2}'.format(url,hostname,outfile), stdout=subprocess.STDOUT).wait()

run(port=7000)